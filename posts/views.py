from django.shortcuts import render, redirect
from .models import *
from django.forms import ModelForm
from django import forms
from bs4 import BeautifulSoup
from django.contrib import messages
import requests

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body']
        labels = {
            'body': 'Caption',
            'url': 'Image URL',
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a caption...'}),
            'url': forms.URLInput(attrs={'placeholder': 'Enter the URL of the image...'}),
        }

def create_post_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            
            website = requests.get(form.data['url'])
            html_code = BeautifulSoup(website.content, 'html.parser')
            
            # find_image = html_code.select('meta[content^="https://live.staticflickr.com/"]')
            # image = find_image[0]['content']
            # or
            
            try:
                image = html_code.select('meta[content^="https://live.staticflickr.com/"]')[0]['content']
            except:
                messages.error(request, 'Invalid URL. Please try again.')
                return redirect('create_post')
            else:
                post_form.image = image
            
            # find_title = html_code.select('h1.photo-title')
            # title = find_title[0].text.strip()
            # or
            title = html_code.select('h1.photo-title')[0].text.strip()
            post_form.title = title
            
            # find_artist = html_code.select('a.owner-name')
            # artist = find_artist[0].text.strip()
            # or
            artist = html_code.select('a.owner-name')[0].text.strip()
            post_form.artist = artist
            
            post_form.save()
            return redirect('home')
    return render(request, 'posts/create_post.html', {'form': form})