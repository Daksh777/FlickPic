from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from django.contrib import messages
import requests
from django.shortcuts import get_object_or_404
from .forms import *

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

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

def delete_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('home')
    return render(request, 'posts/delete_post.html', {'post': post})


def edit_post_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post) # prefill the form with the post 
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('home')
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'posts/edit_post.html', context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'posts/post_page.html', {'post': post})