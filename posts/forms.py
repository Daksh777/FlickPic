from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'url': 'Image URL',
            'tags': 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a caption...'}),
            'url': forms.URLInput(attrs={'placeholder': 'Enter the URL of the image...'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3}),
            'tags': forms.CheckboxSelectMultiple(),
        }