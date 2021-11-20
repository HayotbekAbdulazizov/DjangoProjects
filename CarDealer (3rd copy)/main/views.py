from main.models import  Brand, Category, News, Car, CarImages, NewsImages, Comment
from django.shortcuts import render
# from .models import News, Product
from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, UpdateView,	DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.

def HomePageView(request):
	cars = Car.objects.all()
	context = {
		'cars':cars,
	}
	return render(request, 'index.html',context )



###   CARS
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'car_update.html'
    success_url = '/'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/'