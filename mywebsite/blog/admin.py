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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'body', 'post', 'active')
    list_filter = ('active','create_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)