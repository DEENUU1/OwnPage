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



class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    body = models.TextField()
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering = ['create_date']

    def __str__(self):
        return 'Komentarz {} napisany przez {}'.format(self.body, self.name)
