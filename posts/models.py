from django.db import models
import uuid
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.URLField(max_length=500)
    url = models.URLField(max_length=500, null=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likedposts', blank=True, through="LikedPost")
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']
        
class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.post.title}'
        
class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'No author : {self.body[:30]}'
        
    class Meta:
        ordering = ['-created']
        
        
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'No author : {self.body[:30]}'
        
    class Meta:
        ordering = ['-created']