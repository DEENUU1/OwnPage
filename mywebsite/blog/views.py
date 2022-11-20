from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

def index(request):
  mytitle = Post.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mytitle': mytitle,
  }
  return HttpResponse(template.render(context, request))

# def index(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

