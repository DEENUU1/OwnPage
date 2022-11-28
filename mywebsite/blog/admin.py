from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from .models import *



# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title, date, author, content')

class PostAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()},
    }

admin.site.register(Post)