from main.models import Movie, Rubrics
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView



# Create your views here.

class HomePageView(ListView):
    model = Movie
    template_name = "index.html"

class CategorySortView(DetailView):
    model = Rubrics
    template_name = "category_sort.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'detail.html'