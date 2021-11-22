from django.conf.urls import url
from django.db import models
from django.urls import path
from . import views
from django.views.generic import TemplateView,DetailView
# from .models import Category, Book

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<pk>/', views.CategorySortView.as_view(), name='category_sort'),
    path('detail/<pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    # path('category_filter/<pk>', DetailView.as_view(model=Category, template_name='index.html'), name='category_filter'),

]