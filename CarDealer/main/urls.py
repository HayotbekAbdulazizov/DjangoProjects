from main.models import Car
from django.urls import path
from . import views
# from .models import News, Product
from django.views.generic import TemplateView,  ListView, UpdateView,	DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('cars/',views.searchResult, name='cars'),
    path('search/', views.searchResult, name='search'),
    
    path('car_detail/<int:pk>',views.CarDetailView.as_view ( ), name='car_detail'),
    path('car_update/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
    path('car_delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),


    
    # path('news_details/<pk>', DetailView.as_view(model = News,  template_name = 'news_details.html'), name='news_details'),
    # path('news_update/<pk>', UpdateView.as_view( model = News, template_name = 'news_update.html',     fields = ['title','category','image','body'],     success_url = '/'), name='news_update'),
    # path('news_delete/<pk>', DeleteView.as_view(model=News, template_name='news_delete.html', success_url='/'), name='news_delete'),
    
]