from django.db import models
from BlogApp.models import post
class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 100)
    published_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
