from django.urls import path
from .import views

app_name = 'movie'
urlpatterns = [
    path('', views.MovieListView.as_view(),name='home'),
    path('detail/<slug:slug>/', views.MovieDetailView.as_view(), name='detail'),
    path('search/', views.movieSearch, name='search'),

    path('like/<int:pk>', views.addLike, name='like')
]