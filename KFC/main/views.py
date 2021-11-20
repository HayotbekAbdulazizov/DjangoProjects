from django.shortcuts import redirect, render
from .models import Category, Food
from django.views.generic import DetailView

from main import models
# Create your views here.

def DetailView(request, pk):
    pk2  = int(pk) + 1
    pk_ = str(pk2)
    if pk != 0:
        pk1  = int(pk) - 1
        _pk = str(pk1)
    food = Food.objects.get(id=pk)
    f_food = Food.objects.get(id=_pk)
    food_f = Food.objects.get(id=pk_)
    print(f_food.name)
    print(f_food.id)
    context = {
        'food':food,
        "food_":food_f,
        '_food':f_food,
    }
    return render(request, 'detail.html', context)


