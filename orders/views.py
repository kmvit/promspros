# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from profiles.models import UserProfile
from models import *
from django.views.generic.edit import FormView, CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from forms import *
from django.core.urlresolvers import reverse_lazy
from forms import ContactForm
from django.core.mail import send_mail, EmailMessage, BadHeaderError
import os
import zipfile
import StringIO
from billboard.settings import PROJECT_ROOT
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
import base64
from django.core.files.base import ContentFile
import logging
from django.conf import settings
import json
from django.core import serializers
from django.db import transaction
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.sitemaps import Sitemap




def getfiles(request):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)
    filenames = []
    for thing in OrderImage.objects.filter(order__id=request.GET['q']):
        filenames.append(os.path.join('/home/justscoundrel/billboard/media/', thing.file.name))
    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp    
    
    
def getfiles_sentence(request):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)
    filenames = []
    for thing in SentenceImage.objects.filter(sentence__id=request.GET['q']):
        filenames.append(os.path.join('/home/users1/j/justscoundrel/domains/board.kmv-it.ru/media/', thing.file.name))
    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp 


class Home(ListView):
    model = Order
    template_name = 'index.html'
    context_object_name = 'order_list'
    def get_context_data(self,**kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(status=1)
        context['sentence_list'] = Sentence.objects.filter(status=1)
        context['company_list'] = Company.objects.all()
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context



class OrderList(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'order_list'
    def get_context_data(self,**kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(status=1).order_by('-born')
        context['sentence_list'] = Sentence.objects.all()
        context['company_list'] = Company.objects.all()
        return context
    
class OrderView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    def get_context_data(self,**kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(user=self.object.user, status=1).exclude(pk=self.object.id)
        context['company'] = Company.objects.filter(city=self.object.city).exclude(user=self.object.user)
        context['files'] = OrderImage.objects.filter(order__id=self.object.id)
        return context
    

class OrderCreate(CreateView):
    model = Order
    template_name = 'add_order.html'
    form_class = AddOrderForm
    
    def get_context_data(self,**kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.filter(id=self.request.user.id)
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context
    
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.id})
        

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        form.instance.category = get_object_or_404(Subcategory, title=self.request.POST['category'])
        if 'submit-ch' in self.request.POST:
            form.instance.status = '3'
        self.object = form.save()
        photos = self.request.POST.getlist('photos[]')
        for strg in photos:
            strg =strg.partition('base64,')[2]
            img_data = base64.decodestring(strg)
            photo = OrderImage(order=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
            photo.file.save('123.jpg', ContentFile(img_data))
            photo.save()
        return HttpResponseRedirect(self.get_absolute_url())
        
        
        

class OrderUpdate(UpdateView):
    model = Order
    form_class = EditOrderForm
    template_name = 'edit_order.html'
    def get_context_data(self,**kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context['orderimage_list'] = OrderImage.objects.filter(order=self.object.id)
        return context
    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.id})
        
    def form_valid(self, form):
        if self.request.user == self.object.user:
            self.object = form.save()
            photos = self.request.POST.getlist('photos[]')
            for strg in photos:
                strg =strg.partition('base64,')[2]
                img_data = base64.decodestring(strg)
                photo = OrderImage(order=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
                photo.file.save('123.jpg', ContentFile(img_data))
                photo.save()
            
            return HttpResponseRedirect(self.get_absolute_url())
        else:
            return HttpResponseRedirect(self.get_absolute_url())

class OrderDelete(DeleteView):
    model = Order
    template_name = 'delete_order.html'
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk':self.request.user.userprofile.id})
        
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(OrderDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SentenceList(ListView):
    model = Sentence
    template_name = 'sentence_list.html'
    context_object_name = 'sentence_list'
    def get_context_data(self,**kwargs):
        context = super(SentenceList, self).get_context_data(**kwargs)
        context['company_list'] = Company.objects.all()
        context['sentence_list'] = Sentence.objects.filter(status=1).order_by('-born')
        return context
   
    

class SentenceView(DetailView):
    model = Sentence
    template_name = 'sentence_detail.html'
    def get_context_data(self,**kwargs):
        context = super(SentenceView, self).get_context_data(**kwargs)
        context['files'] = SentenceImage.objects.filter(sentence__id=self.object.id)
        context['sentence_list'] = Sentence.objects.filter(user=self.object.user, status=1).exclude(pk=self.object.id)
        context['company'] = Company.objects.filter(city=self.object.city).exclude(user=self.object.user)
        return context

  
        
class SentenceCreate(CreateView):
    model = Sentence
    template_name = 'add_sentence.html'
    form_class = AddSentenceForm
    
    def get_context_data(self,**kwargs):
        context = super(SentenceCreate, self).get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.filter(id=self.request.user.id)
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context
    
    def get_absolute_url(self):
        return reverse('sentence_detail', kwargs={'pk': self.object.id})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        form.instance.category = get_object_or_404(Subcategory, title=self.request.POST['category'])
        if 'submit-ch' in self.request.POST:
            form.instance.status = '3'
        self.object = form.save()
        photos = self.request.POST.getlist('photos[]')
        for strg in photos:
            strg =strg.partition('base64,')[2]
            img_data = base64.decodestring(strg)
            photo = SentenceImage(sentence=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
            photo.file.save('123.jpg', ContentFile(img_data))
            photo.save()
        return HttpResponseRedirect(self.get_absolute_url())
   
class SentenceUpdate(UpdateView):
    model = Sentence
    form_class = EditSentenceForm
    template_name = 'edit_sentence.html'
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SentenceUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
    
    def get_context_data(self,**kwargs):
        context = super(SentenceUpdate, self).get_context_data(**kwargs)
        context['sentenceimage_list'] = SentenceImage.objects.filter(sentence=self.object.id)
        return context
    
    def get_absolute_url(self):
        return reverse('sentence_detail', kwargs={'pk': self.object.id})
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        if 'submit-ch' in self.request.POST:
            form.instance.status = '3'
        self.object = form.save()
        photos = self.request.POST.getlist('photos[]')
        for strg in photos:
            strg =strg.partition('base64,')[2]
            img_data = base64.decodestring(strg)
            photo = SentenceImage(sentence=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
            photo.file.save('123.jpg', ContentFile(img_data))
            photo.save()
        return HttpResponseRedirect(self.get_absolute_url())
    
    def manage_images(request):
        ImageFormSet = formset_factory(form_class)
        if request.method == 'POST':
            formset = ImageFormSet(request.POST, request.FILES)
            if formset.is_valid():
                for f in request.FILES:
                    image = form_class(request.POST, f)
                    image.save()
        else:
            formset = ImageFormSet()
        return render_to_response('manage_images.html', {'formset': formset})
    
class SentenceDelete(DeleteView):
    model = Sentence
    template_name = 'delete_sentence.html'
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SentenceDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk':self.request.user.userprofile.id})


class CompanyList(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'company_list'
    def get_context_data(self,**kwargs):
        context = super(CompanyList, self).get_context_data(**kwargs)
        context['company_list'] = Company.objects.all().exclude(user__pk=self.request.user.pk)
        return context
    
class CompanyView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    def get_context_data(self,**kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(user=self.object.user, status=1)
        context['order_count'] = Order.objects.filter(user=self.object.user, status=1).count()
        context['sentence_count'] = Sentence.objects.filter(user=self.object.user, status=1).count()
        context['sentence_list'] = Sentence.objects.filter(user=self.object.user, status=1)
        
        return context



class CompanyCreate(CreateView):
    model = Company
    template_name = 'add_company.html'
    form_class = AddCompanyForm
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.request.user.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        photos = self.request.POST.getlist('photos[]')
        for strg in photos:
            strg =strg.partition('base64,')[2]
            img_data = base64.decodestring(strg)
            photo = CompanyImage(order=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
            photo.file_up.save('123.jpg', ContentFile(img_data))
            photo.save()
            
        return HttpResponseRedirect(self.get_absolute_url())



class CompanyUpdate(UpdateView):
    model = Company
    form_class = AddCompanyForm
    template_name = 'edit_company.html'
    def get_context_data(self, **kwargs):
        context = super(CompanyUpdate, self).get_context_data(**kwargs)
        context['companyimage_list'] = CompanyImage.objects.filter(order=self.object.id)
        if self.request.POST:
            context['form'] = AddCompanyForm(self.request.POST, instance=self.object)
        return context
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(CompanyUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
        
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.request.user.id})
    
    @login_required                                                               
    def edit_profile(self, request, pk):                                                      
        company = get_object_or_404(Company, id=pk)                                      
        if self.request.user != company.user:                                              
            raise Http404()
        
    def form_valid(self, form):
        self.object = form.save()
        photos = self.request.POST.getlist('photos[]')
        for strg in photos:
            strg =strg.partition('base64,')[2]
            img_data = base64.decodestring(strg)
            photo = CompanyImage(order=self.object)

            # Не знаю какая у вас логика формирования имён файлов,
            # добавьте какой-нибудь код определяющий file_name.
            # Я обычно генерирую md5-хэш данных.
            photo.file_up.save('123.jpg', ContentFile(img_data))
            photo.save()
            
        return HttpResponseRedirect(self.get_absolute_url())

        
class CompanyDelete(DeleteView):
    model = Company
    template_name = 'delete_company.html'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(CompanyDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk':self.request.user.userprofile.id})    
    
    

class SearchList(ListView):
    model = Order
    template_name = 'search_list.html'
    def get_context_data(self,**kwargs):
        context = super(SearchList, self).get_context_data(**kwargs)
        if self.request.GET['city'] == '' and self.request.GET['s'] == 'order':
            context['search_list'] = Order.objects.filter(title__icontains=self.request.GET['q'], status=1)
        elif self.request.GET['city'] == '' and self.request.GET['s'] == 'sentence':
            context['search_list'] = Sentence.objects.filter(title__icontains=self.request.GET['q'], status=1)
        elif self.request.GET['city'] == '' and self.request.GET['s'] == 'company':
            context['search_list'] = Company.objects.filter(title__icontains=self.request.GET['q'])
        elif self.request.GET['city'] != '' and self.request.GET['s'] == 'order':
            context['search_list'] = Order.objects.filter(title__icontains=self.request.GET['q'], city=self.request.GET['city'], status=1)
        elif self.request.GET['city'] != '' and self.request.GET['s'] == 'sentence':
            context['search_list'] = Sentence.objects.filter(title__icontains=self.request.GET['q'], city=self.request.GET['city'], status=1)
        elif self.request.GET['city'] != '' and self.request.GET['s'] == 'company':
            context['search_list'] = Company.objects.filter(title__icontains=self.request.GET['q']).exclude(user__pk=self.request.user.pk)
        context['modeltype'] = self.request.GET['s'] 
        return context    

        
class SearchCityList(ListView):
    model = Order
    template_name = 'search_list.html'
    def get_context_data(self, **kwargs):
        context = super(SearchCityList, self).get_context_data(**kwargs)
        object_model_name =  self.request.GET['modeltype']
        if self.request.GET['city'] and object_model_name == 'order':
            context['search_list'] = Order.objects.filter(city=self.request.GET['city'], status=1)
            context['search_list_count'] = Order.objects.filter(city=self.request.GET['city'], status=1).count()
        elif self.request.GET['city'] and object_model_name == 'company':
            context['search_list'] = Company.objects.filter(city=self.request.GET['city'])
            context['search_list_count'] = Company.objects.filter(city=self.request.GET['city'], status=1).count()
        else:
            context['search_list'] = Sentence.objects.filter(city=self.request.GET['city'], status=1)
            context['search_list_count'] = Sentence.objects.filter(city=self.request.GET['city'], status=1).count()
        context['modeltype'] = object_model_name
        return context 
        
class PageView(DetailView):
     
    template_name = 'page_detail.html'
    context_object_name = 'page'
    model = Page
    
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['form'] = ContactForm
        return context
    
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            

class CategoryView(DetailView):
    model = Category
    template_name = 'category_list.html'
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['subcategory_list'] = Subcategory.objects.filter(parent_id=self.kwargs['pk'])
        context['order_list'] = Order.objects.filter(category__parent_id=self.kwargs['pk'])
        context['sentence_list'] = Sentence.objects.filter(category__parent_id=self.kwargs['pk'])
        return context

            
class SubcategoryDetail(DetailView):
    model = Subcategory
    template_name = 'subcategory.html'
    def get_context_data(self, **kwargs):
        context = super(SubcategoryDetail, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(category_id=self.kwargs['pk'])
        context['sentence_list'] = Sentence.objects.filter(category_id=self.kwargs['pk'])
        return context

            
def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST,request.FILES)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			recipients = ['justscoundrel@yandex.ru']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			try:
				mail = EmailMessage(subject, message, 'registry@promspros.ru', ['info@promspros.ru',])
				mail.send()
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'contact.html', {'form': form})

def robots(request):
    return render_to_response('robots.txt', content_type='text/plain')	
	
	
