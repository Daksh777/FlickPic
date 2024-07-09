from django.forms import ModelForm
from .models import *
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'avatar': 'Profile Picture',
            'realname': 'Name'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput()
        }