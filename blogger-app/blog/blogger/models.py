from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    username = models.CharField(max_length=150,default="")
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("comments", kwargs={'pk':self.pk})