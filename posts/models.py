from django.db import models
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    url = models.URLField(max_length=500, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-created']