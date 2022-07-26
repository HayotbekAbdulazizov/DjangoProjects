from django.urls import path, include
from . import views



app_name = 'main'

urlpatterns = [
    # path('', views.HomePageView.as_view(), name="home_page"),
    path('', views.pj1, name="pj1"),
    path('pj2', views.pj2, name="pj2"),
    # path('articles/', views.ArticleView.as_view(), name="article_view"),
    # path('categories/', views.CategoryView.as_view(), name="category_view"),
    # path('tags`/', views.TagView.as_view(), name="tag_view"),
]