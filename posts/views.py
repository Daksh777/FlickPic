from django.shortcuts import render
from .models import *

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})