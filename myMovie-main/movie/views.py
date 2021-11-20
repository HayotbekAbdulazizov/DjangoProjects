from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.views.generic import  (
    TemplateView,
    ListView,
    DetailView
    )
from .models import Rubrics, Movie
# Create your views here.
def get_all_rubrics(request):
    context = {
        'rubrics':Rubrics.objects.all()
    }
    return context

class MovieListView(ListView):
    model = Movie
    paginate_by = 8
    template_name = 'index.html'

class MovieDetailView(DetailView):
    model = Movie

    
import json
def movieSearch(request):
    data = {}
    query = request.GET.get('data')
    movies = list(Movie.objects.filter(slug__icontains=query).values())
    data['data'] = movies
    return JsonResponse(data)

def addLike(request, pk):
    print(type(pk))
    movie = Movie.objects.get(id=pk)
    movie.like += 1
    movie.save()
    return redirect('movie:detail',movie.slug)