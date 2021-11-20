from django.conf.urls import url
from django.db import models
from django.urls import path
from . import views
from django.views.generic import TemplateView,DetailView
from .models import Category, Book

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('detail/<pk>', DetailView.as_view(model=Book, template_name='detail.html'), name='detail_page'),
    path('category_filter/<pk>', DetailView.as_view(model=Category, template_name='index.html'), name='category_filter'),

]