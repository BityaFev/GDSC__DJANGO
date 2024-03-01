from django.db import models

class post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category = models.CharField(max_length = 100)
    image = models.ImageField()
    
    def str(self):
        return self.title
