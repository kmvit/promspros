# -*- coding: utf-8 -*-
from django import forms
from models import *
from tinymce.widgets import TinyMCE


class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100, required=True)
    sender = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs.update({'class': 'main-input', 'required': True})


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', 'status', 'born', 'category', 'slug']


class EditOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', 'status', 'email', 'born', 'category', 'slug']

    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'


class AddSentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = '__all__'
        exclude = ['user', 'status', 'born', 'category', 'slug']
        widgets = {
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }


class EditSentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = '__all__'
        exclude = ['user', 'status', 'born', 'email', 'category', 'slug']

    def __init__(self, *args, **kwargs):
        super(EditSentenceForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddCompanyForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'
