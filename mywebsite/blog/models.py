from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title + ' | ' + str(self.author)


