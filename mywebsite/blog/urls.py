from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    # path('register', views.register_request, name='register')
    # path('', views.index, name='index')
]