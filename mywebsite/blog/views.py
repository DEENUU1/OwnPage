
from .models import Post
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

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

