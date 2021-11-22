from shutil import move
from main.models import Movie, Rubrics
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, View, DetailView
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.urls import reverse


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

def MovieDetailView(request, pk):
    movie = Movie.objects.get(id=pk)
    related_movies = Movie.objects.filter(rubric=movie.rubric).order_by('?')[:6]
    context = {
        'movie':movie,
        'related_movies':related_movies,
    }
    return render(request, 'detail.html', context)

def artists_view(request):
    all_movies = Movie.objects.all()
    ctx = {
        'all_movies':all_movies,
    }
    url_parameter = request.GET.get("q")

    if url_parameter:
        artists = Movie.objects.filter(slug__icontains=url_parameter)
        ctx["searched_movies"] = artists
    else:
        ctx['none']= None

    if request.is_ajax():
        html = render_to_string(
            template_name="search_result.html", context={"searched_movies": artists}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "index.html", context=ctx)






def AddLike(request, pk):
    movie = Movie.objects.get(id=int(pk))
    # if request.user.is_authenticated():
    #     if movie.likes.filter(id=request.user.id).exists():
        #     # movie.likes.remove(request.user)
        # # else:
        # #     movie.likes.add(request.user)
        # movie.save()
    return reverse('main:home') 