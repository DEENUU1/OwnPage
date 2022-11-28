from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = HTMLField()
    body_short = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    time_reading = models.TextField()




    def __str__(self):
        return self.title + ' | ' + str(self.author)


