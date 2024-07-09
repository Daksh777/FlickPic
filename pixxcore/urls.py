"""
URL configuration for pixxcore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import *
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('post/create/', create_post_view, name='create_post'),
    path('post/delete/<pk>/', delete_post_view, name='delete_post'),
    path('post/edit/<pk>/', edit_post_view, name='edit_post'),
    path('post/<pk>/', post_page_view, name='post'),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)