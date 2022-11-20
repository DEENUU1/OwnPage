from django.db import models
from django.db.models import Model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()