# from main.models import Car`
from django.urls import path
from . import views
# from .models import News, Product
from django.views.generic import TemplateView,  ListView, UpdateView,	DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

app_name = 'main'

urlpatterns = [
    path('', views.HomePage, name='home'),
    # path('detail/<pk>', views.FilterPage, name='filter')
]