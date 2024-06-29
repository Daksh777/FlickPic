from django.shortcuts import render

def home_view(request):
    title = 'Welcome to Pixxcore'
    return render(request, 'posts/home.html', {'title': title})