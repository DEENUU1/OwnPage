from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView, DetailView

class HomeView(ListView):
  model = Post
  template_name = 'index.html'

class ArticleDetailView(DetailView):
  model = Post
  template_name = 'article_details.html'


# def index(request):
#   mytitle = Post.objects.all().values()
#   template = loader.get_template('index.html')
#   context = {
#     'mytitle': mytitle,
#   }
#   return HttpResponse(template.render(context, request))

# def index(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

