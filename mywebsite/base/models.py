from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.subject
