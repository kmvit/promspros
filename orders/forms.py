# -*- coding: utf-8 -*-
from django import forms
from models import *
from tinymce.widgets import TinyMCE
from multiupload.fields import MultiFileField
from django.forms.models import inlineformset_factory
from django.forms.formsets import formset_factory


class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)
	def __init__(self, *args, **kwargs):
	    super(ContactForm, self).__init__(*args, **kwargs)
	    for myField in self.fields:
	        self.fields['message'].widget.attrs['class'] = 'main-textarea'
	        self.fields[myField].widget.attrs['class'] = 'main-input'
	

class AddOrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user','status','email','born','category']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }
    
        
class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user','status','email','born']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }
    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'
        
   
        
class AddSentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = '__all__'
        exclude = ['user','status','email','born']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }
        


class EditSentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = '__all__'
        exclude = ['user','status','born','email']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }
    def __init__(self, *args, **kwargs):
        super(EditSentenceForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'info': TinyMCE(attrs={'cols': 60, 'rows': 10}),
        }
    def __init__(self, *args, **kwargs):
        super(AddCompanyForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'
        

        
        

