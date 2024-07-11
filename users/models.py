from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    realname = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    @property
    def get_avatar(self):
        try:
            avatar_url = self.image.url
        except:
            avatar_url = static('images/avatar_default.svg')
            
        return avatar_url


    @property
    def get_realname(self):
        return self.realname if self.realname else self.user.username