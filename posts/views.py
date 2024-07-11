from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from django.contrib import messages
import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *

def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
        
    categories = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag
    }
    
    return render(request, 'posts/home.html', context)

@login_required
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
            
            post_form.author = request.user
            
            post_form.save()
            messages.success(request, 'Post created successfully.')
            form.save_m2m()
            return redirect('home')
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('home')
    return render(request, 'posts/delete_post.html', {'post': post})

@login_required
def edit_post_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
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