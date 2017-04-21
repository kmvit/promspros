# -*- coding: utf-8 -*-
from django import forms
from models import *
from tinymce.widgets import TinyMCE


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','name','phone', 'email']
    def __init__(self, *args, **kwargs):
        super(AddProfileForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'
            
            
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','name','phone']
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'main-input'