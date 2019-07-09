from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from models import *
from orders.models import *
from forms import *
from django.views.generic.edit import FormView, CreateView,UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
import zipfile
from django.contrib.auth.decorators import permission_required
# Create your views here.

class ProfileListView(ListView):
    model = User
    template_name = 'list_profile.html'
    context_object_name = 'profile_list'


class ProfileView(DetailView):
    model = UserProfile
    template_name = 'userprofile.html'
    context_object_name = 'profile'
    def get_context_data(self,**kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.filter(user=self.request.user).count()
        context['order_activ'] = Order.objects.filter(user=self.request.user, status = 1).count()
        context['order_noactiv'] = Order.objects.filter(user=self.request.user, status = 2).count()
        context['order_che'] = Order.objects.filter(user=self.request.user, status = 3).count()
        context['sentence_activ'] = Sentence.objects.filter(user=self.request.user, status = 1).count()
        context['sentence_noactiv'] = Sentence.objects.filter(user=self.request.user, status = 2).count()
        context['sentence_che'] = Sentence.objects.filter(user=self.request.user, status = 3).count()
        context['active'] = Sentence.objects.filter(user=self.request.user, status = 1).count() + Order.objects.filter(user=self.request.user, status = 1).count()
        context['noactive'] = Sentence.objects.filter(user=self.request.user, status = 2).count() + Order.objects.filter(user=self.request.user, status = 2).count()
        context['che'] = Sentence.objects.filter(user=self.request.user, status = 3).count() + Order.objects.filter(user=self.request.user, status = 3).count()
        
        return context
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


class ProfileUpdate(UpdateView):
    model = UserProfile
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    def get_context_data(self,**kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.filter(id=self.object.id)
        return context
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUpdate, self).dispatch(*args, **kwargs)
        

    
class NotCompanyView(DetailView):
    model = UserProfile
    template_name = 'notcompany.html'
    context_object_name = 'profile'
    def get_context_data(self,**kwargs):
        context = super(NotCompanyView, self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(user=self.object.userprofile).order_by('-born')
        context['sentence_list'] = Sentence.objects.filter(user=self.object.userprofile).order_by('-born')
        context['order_count'] = Order.objects.filter(user=self.object.userprofile).count()
        context['sentence_count'] = Sentence.objects.filter(user=self.object.userprofile).count()
        return context
