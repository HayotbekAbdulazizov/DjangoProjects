from django.conf.urls import url
from django.db import models
from django.urls import path
from . import views
from django.views.generic import TemplateView, DetailView
from .models import Food


app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('detail/<pk>', views.DetailView, name='food_detail')

]