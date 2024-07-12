from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category    = models.CharField(max_length=255)
    author      = models.CharField(max_length=255)
    created     = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
