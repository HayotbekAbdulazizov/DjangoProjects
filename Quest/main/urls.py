from django.conf.urls import url
from django.db import models
from django.urls import path
from . import views
from django.views.generic import TemplateView, DetailView, ListView
from .models import Quest


app_name = 'main'

urlpatterns = [
    path('', ListView.as_view(model=Quest,template_name='index.html')),
    # path('detail/<pk>', DetailView.as_view(model=Food,template_name='detail.html'), name='food_detail')

]