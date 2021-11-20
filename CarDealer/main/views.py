from main.models import  Brand, Category, News, Car, CarImages, NewsImages, Comment
from django.shortcuts import render
# from .models import News, Product
from django.shortcuts import render
from django.views.generic import TemplateView,  ListView, UpdateView,	DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.

def HomePageView(request):
    cars = Car.objects.all()
    news = News.objects.all().order_by('comments')
    exp_cars = Car.objects.all().order_by('price')[:5]
    m_exp_car = exp_cars[0]
    print(m_exp_car.brand)
    print(m_exp_car.brand)
    print(type(m_exp_car))
    print(m_exp_car.image_main)
    for ne in  news:
        print(ne.title)
    context = {
        'cars':cars,
        'news':news,
        "exp_cars":exp_cars,
        'm_exp_car':m_exp_car,
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



####   Search bar
def searchResult(request):
    cars = Car.objects.all()
    if request.method == 'GET':
        status = request.GET.get('used_new',None)
        company_input = request.GET.get('company',None)
        category = request.GET.get('category',None)
        fuel = request.GET.get('fuel',None)

        if status != None:
            cars = Car.objects.filter(status=status)


        for car in cars:
            pass  
        
        
        # cars = Car.objects.filter(model__icontains=q)
    context = {
        'cars':cars,
    }
    return render(request, 'cars.html', context)



# https://www.phpjabbers.com/free-car-dealer-website-templates.php



"""
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
https://freehtmldesigns.com/vehicle-html-website-templates/
"""