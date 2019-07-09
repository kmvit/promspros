# -*- coding: utf-8 -*-
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import MultipleObjectMixin
from endless_pagination.models import PageList

from orders.helpers import get_first_grouped_items
from profiles.models import UserProfile
from models import *
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from forms import *
from forms import ContactForm
from django.core.mail import EmailMessage, BadHeaderError
import os
import zipfile
import StringIO
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseNotAllowed
import base64
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


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


class VisitedMixin(ListView):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseNotAllowed(['POST', ])

        key = 'is_hide__{}'.format(request.POST.get('page', ''))
        request.session[key] = not request.session.get(key, False)
        return self.get(request, *args, **kwargs)


class PaginatedViewMixin(MultipleObjectMixin):

    per_page = settings.NUMBER_OF_RECORDS

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name(queryset)
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.per_page)
        self.paginate_by = len(page)
        context = {
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated,
            'object_list': queryset
        }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        context['show_pages'] = PageList(self.request, context['page_obj'], 'page')
        if 'view' not in context:
            context['view'] = self
        return context


class PaginatePageMixin(Paginator):
    model_class = Order

    def page(self, number):
        number = self.validate_number(number)
        per_page = settings.NUMBER_OF_RECORDS
        bottom = (number - 1) * per_page
        id__in = self.object_list.values_list('id', flat=True)
        object_list, self._count = get_first_grouped_items(self.model_class, id__in, from_idx=bottom, n=per_page)
        self._num_pages = None
        return self._get_page(object_list, number, self)


class CustomOrderPaginator(PaginatePageMixin):
    model_class = Order


class CustomSentencePaginator(PaginatePageMixin):
    model_class = Sentence


class Home(VisitedMixin):
    model = Order
    template_name = 'index.html'
    context_object_name = 'order_list'

    def get_context_data(self,**kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        category_list = Subsubcategory.objects.all()
        counts = []
        for category in category_list:
            counts.append(str(category.order_set.all().count() + category.sentence_set.all().count()))
        context['counts'] = counts
        context['block_page'] = BlockonPage.objects.get(id=1)

        f1 = {'status': 1}
        e1 = {}
        is_hide = self.request.session.get('is_hide__order', False)
        if is_hide:
            visited = self.request.session.get('visited_orders', [])
            e1['id__in'] = visited
        id__in1 = Order.objects.filter(**f1).exclude(**e1).values_list('id', flat=True)
        context['order_list'], _ = get_first_grouped_items(Order, id__in1, from_idx=0, n=settings.NUMBER_OF_RECORDS)

        f2 = {'status': 1}
        e2 = {}
        is_hide = self.request.session.get('is_hide__sentence', False)
        if is_hide:
            visited = self.request.session.get('visited_sentences', [])
            e2['id__in'] = visited
        id__in2 = Sentence.objects.filter(**f2).exclude(**e2).values_list('id', flat=True)
        context['sentence_list'], _ = get_first_grouped_items(Sentence, id__in2, from_idx=0, n=settings.NUMBER_OF_RECORDS)

        context['category_list'] = Category.objects.all()
        return context


class OrderList(VisitedMixin, PaginatedViewMixin):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'order_list'
    paginator_class = CustomOrderPaginator

    def get_queryset(self):
        object_list = Order.objects.filter(status=1).order_by('-born')
        is_hide = self.request.session.get('is_hide__order', False)
        if is_hide:
            visited_orders = self.request.session.get('visited_orders', [])
            object_list = object_list.exclude(id__in=visited_orders)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['block_page'] = BlockonPage.objects.get(id=3)
        return context


class OrderView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self,**kwargs):
        visited_orders = self.request.session.get('visited_orders', [])
        if self.object.id not in visited_orders:
            visited_orders.append(self.object.id)
            self.request.session['visited_orders'] = visited_orders
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
        return reverse('order_detail', kwargs={
            'category_slug': self.object.category.parent.parent.slug,
            'subcategory_pk': self.object.category.parent.id,
            'subsubcategory_slug': self.object.category.slug,
            'slug': self.object.slug,
        })

    def form_valid(self, form):
        messages.error(self.request, u'Ваше объявление добавлено!')
        form.instance.user = self.request.user
        form.instance.category = get_object_or_404(Subsubcategory, title=self.request.POST['category'])
        form.instance.slug = slugify(unidecode(form.cleaned_data['title']))
        form.instance.city = form.cleaned_data['city'].title()
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


class OrderUpdate(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = EditOrderForm
    template_name = 'edit_order.html'
    success_message = 'Ваше объявление отредактировано!'

    def get_context_data(self,**kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context['orderimage_list'] = OrderImage.objects.filter(order=self.object.id)
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'category_slug': self.object.category.parent.parent.slug, 'subcategory_pk': self.object.category.parent.id, 'subsubcategory_slug': self.object.category.slug, 'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Subsubcategory, title=self.request.POST['category'])
        messages.error(self.request, u'Ваше объявление отредактировано!')
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


class SentenceList(VisitedMixin, PaginatedViewMixin):
    model = Sentence
    template_name = 'sentence_list.html'
    context_object_name = 'sentence_list'
    paginator_class = CustomSentencePaginator

    def get_queryset(self):
        object_list = Sentence.objects.filter(status=1).order_by('-born')
        is_hide = self.request.session.get('is_hide__sentence', False)
        if is_hide:
            visited_sentences = self.request.session.get('visited_sentences', [])
            object_list = object_list.exclude(id__in=visited_sentences)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SentenceList, self).get_context_data(**kwargs)
        context['block_page'] = BlockonPage.objects.get(id=2)
        return context


class SentenceView(DetailView):
    model = Sentence
    template_name = 'sentence_detail.html'

    def get_context_data(self,**kwargs):
        visited_sentences = self.request.session.get('visited_sentences', [])
        if self.object.id not in visited_sentences:
            visited_sentences.append(self.object.id)
            self.request.session['visited_sentences'] = visited_sentences
        context = super(SentenceView, self).get_context_data(**kwargs)
        context['files'] = SentenceImage.objects.filter(sentence__id=self.object.id)
        context['sentence_list'] = Sentence.objects.filter(user=self.object.user, status=1).exclude(pk=self.object.id)
        context['company'] = Company.objects.filter(city=self.object.city).exclude(user=self.object.user)
        return context


class SentenceCreate(CreateView):
    model = Sentence
    template_name = 'add_sentence.html'
    form_class = AddSentenceForm
    success_message = 'Ваше объявление отредактировано!'

    def get_context_data(self,**kwargs):
        context = super(SentenceCreate, self).get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.filter(id=self.request.user.id)
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('sentence_detail', kwargs={'category_slug': self.object.category.parent.parent.slug, 'subcategory_pk': self.object.category.parent.id, 'subsubcategory_slug': self.object.category.slug, 'slug': self.object.slug})

    def form_valid(self, form):
        messages.error(self.request, u'Ваше объявление добавлено!')
        form.instance.user = self.request.user
        form.instance.category = get_object_or_404(Subsubcategory, title=self.request.POST['category'])
        form.instance.slug = slugify(unidecode(form.cleaned_data['title']))
        form.instance.city = form.cleaned_data['city'].title()
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


class SentenceUpdate(SuccessMessageMixin, UpdateView):
    model = Sentence
    form_class = EditSentenceForm
    template_name = 'edit_sentence.html'
    success_message = 'Ваше объявление отредактировано!'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SentenceUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def get_context_data(self,**kwargs):
        context = super(SentenceUpdate, self).get_context_data(**kwargs)
        context['sentenceimage_list'] = SentenceImage.objects.filter(sentence=self.object.id)
        context['category_list'] = Category.objects.all()
        context['subcategory_list'] = Subcategory.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('sentence_detail', kwargs={
            'category_slug': self.object.category.parent.parent.slug,
            'subcategory_pk': self.object.category.parent.id,
            'subsubcategory_slug': self.object.category.slug,
            'slug': self.object.slug
        })

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Subsubcategory, title=self.request.POST['category'])
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
        messages.error(self.request, u'Ваше объявление отредактировано!')
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


class CompanyList(VisitedMixin):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'company_list'
    paginate_by = settings.COMPANY_NUMBER_OF_RECORDS

    def get_queryset(self):
        object_list = Company.objects.all().exclude(user__pk=self.request.user.pk).order_by('-id')
        is_hide = self.request.session.get('is_hide__company', False)
        if is_hide:
            visited_companies = self.request.session.get('visited_companies', [])
            object_list = object_list.exclude(id__in=visited_companies)
        return object_list

    def get_context_data(self, **kwargs):
        object_list = self.get_queryset()
        context = super(CompanyList, self).get_context_data(object_list=object_list, **kwargs)
        context['block_page'] = BlockonPage.objects.get(id=4)
        context['show_pages'] = PageList(self.request, context['page_obj'], 'page')
        return context


class CompanyView(DetailView):
    model = Company
    template_name = 'company_detail.html'

    def get_context_data(self,**kwargs):
        visited_companies = self.request.session.get('visited_companies', [])
        if self.object.id not in visited_companies:
            visited_companies.append(self.object.id)
            self.request.session['visited_companies'] = visited_companies
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

    def get_context_data(self, **kwargs):
        context = super(CompanyCreate, self).get_context_data(**kwargs)
        context['company'] = Company.objects.filter(user=self.request.user)
        return context

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


class SearchList(VisitedMixin):
    model = Order
    template_name = 'search_list.html'
    context_object_name = 'search_list'
    paginate_by = settings.COMPANY_NUMBER_OF_RECORDS

    def get_queryset(self):
        object_model = None
        qs = None

        city = self.request.GET.get('city', '').title()
        s = self.request.GET.get('s')
        query = self.request.GET.get('q', '')

        if s in ('order', 'sentence'):
            object_model = Order if s == 'order' else Sentence
            qs = (Q(title__icontains=query) |
                  Q(title__icontains=query.title()) |
                  Q(body__icontains=query) |
                  Q(body__icontains=query.title()))
            qs &= Q(status=1)
            if city != '':
                qs &= (Q(city=city) | Q(city=city.lower()))

        elif s == 'company':
            object_model = Company
            qs = (Q(title__icontains=query) |
                  Q(title__icontains=query.title()) |
                  Q(info__icontains=query) |
                  Q(info__icontains=query.title()))
            if city != '':
                qs &= (Q(city=city) | Q(city=city.lower()))

        if object_model:
            object_list = object_model.objects.filter(qs)
            is_hide = self.request.session.get('is_hide__search', False)
            if is_hide:
                if s == 'order':
                    visited = self.request.session.get('visited_orders', [])
                elif s == 'sentence':
                    visited = self.request.session.get('visited_sentences', [])
                elif s == 'company':
                    visited = self.request.session.get('visited_companies', [])
                else:
                    visited = []
                if len(visited):
                    object_list = object_list.exclude(id__in=visited)
        else:
            object_list = Company.objects.none()

        return object_list

    def get_context_data(self, **kwargs):
        object_list = self.get_queryset()
        context = {'search_list_count': len(object_list)}
        ctx = super(SearchList, self).get_context_data(object_list=object_list, **kwargs)
        context.update(ctx)
        context['city'] = self.request.GET.get('city', '').title()
        context['modeltype'] = self.request.GET.get('s', '')
        context['query'] = self.request.GET.get('q', '')
        context['show_pages'] = PageList(self.request, context['page_obj'], 'page')
        return context


class SearchCityList(VisitedMixin):
    model = Order
    template_name = 'search_list.html'
    paginate_by = settings.COMPANY_NUMBER_OF_RECORDS
    context_object_name = 'search_list'

    def get_queryset(self):
        object_model_name = self.request.GET.get('modeltype', '')
        city = self.request.GET.get('city', '').title()

        if city and object_model_name == 'order':
            qs = (Q(city=city) | Q(city=city.lower()))
            qs &= Q(status=1)
            search_list = Order.objects.filter(qs)
        elif city and object_model_name == 'company':
            qs = (Q(city=city) | Q(city=city.lower()))
            search_list = Company.objects.filter(qs)
        else:
            qs = (Q(city=city) | Q(city=city.lower()))
            qs &= Q(status=1)
            search_list = Sentence.objects.filter(qs)

        is_hide = self.request.session.get('is_hide__search', False)
        if is_hide:
            if object_model_name == 'order':
                visited = self.request.session.get('visited_orders', [])
            elif object_model_name == 'sentence':
                visited = self.request.session.get('visited_sentences', [])
            elif object_model_name == 'company':
                visited = self.request.session.get('visited_companies', [])
            else:
                visited = []
            if len(visited):
                search_list = search_list.exclude(id__in=visited)
        return search_list

    def get_context_data(self, **kwargs):
        context = super(SearchCityList, self).get_context_data(**kwargs)
        context['modeltype'] = self.request.GET.get('modeltype', '')
        context['city'] = self.request.GET.get('city', '').title()
        context['query'] = self.request.GET.get('q', '')
        context['show_pages'] = PageList(self.request, context['page_obj'], 'page')
        context['search_list_count'] = context['paginator'].count
        return context


class PageView(DetailView):

    template_name = 'page_detail.html'
    context_object_name = 'page'
    model = Page

    def get_context_data(self, **kwargs):
        return super(PageView, self).get_context_data(form=ContactForm, **kwargs)


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class CategoryView(DetailView):
    model = Category
    template_name = 'category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_list = Subcategory.objects.filter(parent__slug=self.kwargs['slug'])
        order_list = Order.objects.filter(category__parent__parent__slug=self.kwargs['slug'])
        sentence_list = Sentence.objects.filter(category__parent__parent__slug=self.kwargs['slug'])
        context['subcategory_list'] = category_list
        context['order_list'] = order_list
        context['sentence_list'] = sentence_list

        return context


class SubcategoryDetail(DetailView):
    model = Subcategory
    template_name = 'subcategory.html'

    def get_object(self):
        return get_object_or_404(Subcategory, slug=self.kwargs['subcategory_slug'])

    def get_context_data(self, **kwargs):
        context = super(SubcategoryDetail, self).get_context_data(**kwargs)
        category_list = Subsubcategory.objects.filter(parent__slug=self.kwargs['subcategory_slug'])
        context['subcategory_list'] = category_list
        context['category_list'] = Subcategory.objects.filter(parent__slug=self.kwargs['slug'])
        cat = Subcategory.objects.get(slug=self.kwargs['subcategory_slug'])
        context['url_item'] = cat.id
        context['order_list'] = Order.objects.filter(category__parent__slug=self.kwargs['subcategory_slug'], status=1)
        context['sentence_list'] = Sentence.objects.filter(category__parent__slug=self.kwargs['subcategory_slug'], status=1)
        return context


class SubsubcategoryDetail(DetailView):
    model = Subsubcategory
    template_name = 'subsubcategory.html'

    def get_object(self):
        return Subsubcategory.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(SubsubcategoryDetail, self).get_context_data(**kwargs)
        context['category_list'] = Subsubcategory.objects.filter(parent__slug=self.kwargs['subcategory_slug']).exclude(slug=self.kwargs['slug'])
        context['order_list'] = Order.objects.filter(category__slug=self.kwargs['slug'], status=1)
        context['sentence_list'] = Sentence.objects.filter(category__slug=self.kwargs['slug'], status=1)
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

