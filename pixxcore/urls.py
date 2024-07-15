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
    path('<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/delete/', profile_delete_view, name='profile_delete'),
    path('profile/onboarding/', profile_edit_view, name='profile_onboarding'),
    path('commentsent/<pk>/', comment_sent, name='comment_sent'),
    path('comment/delete/<pk>/', comment_delete_view, name='comment_delete'),
    path('replysent/<pk>/', reply_sent, name='reply_sent'),
    path('reply/delete/<pk>/', reply_delete_view, name='reply_delete'), 
    path('post/like/<pk>/', like_post_view, name='like_post'),
    path('comment/like/<pk>', like_comment_view, name='like_comment'),
    path('reply/like/<pk>', like_reply_view, name='like_reply'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)