from os import name
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter   # REST-Framework    


# Routers 

# router = DefaultRouter()
# router.register('article', views.ArticleViewSet, basename='article')

# Routers
# from rest_framework import routers, urlpatterns
# router = routers.SimpleRouter()
# router.register('viewset/articles', views.ArticleViewSet, basename='articles')



app_name = 'api_basic'

urlpatterns = [
    # viewsets and routers
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),



    # genreric view
    # path('generic/article/', views.GenericAPIView.as_view(), name='articles_generic_view_class'),
    # path('generic/detail/<int:id>', views.GenericDetailAPIView.as_view(), name='detail_generic_class_view'),

    # class Based views and Parsers 
    # path('article/', views.ArticleAPIView.as_view(), name='articles_class_based_view'),
    # path('detail/<int:pk>', views.ArticleDetails.as_view(), name='detail_page_class_based_view'),
    
    # Function Based views
    # path('article/', views.homePage),   
    # path('detail/<int:pk>', views.article_detail),   

    # funtion based and clas based views api
    # path('articles/detail/', views.homePage, name='home'),
    # path('articles/all/', views.articleDetail),
    # path('class/articles', views.HomePageAPIView.as_view(), name='Home'),


    # with generics
    # path('generic/articles', views.HomePageGAPIView.as_view(), name='Home'),
    # path('generic/articles/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),

# With ViewSets
    # path('viewset/articles/', views.ArticleViewSet.as_view({'get':'list'}), name='viewset_articles'),
    # path('viewset/article/<int:pk>', views.ArticleViewSet.as_view({'get':'retrieve'}), name='viewset_article'),


# Routers
    # path('', include((router.urls, 'main'), namespace='article')),

# Renderers
    # path('rend/articles/', views.ArticleCountView.as_view(), name='article_count_render'),
    # path('rendfunc/articles/', views.article_count_view, name='article_count_render_func')






# API view
    path('', views.GitProfileAPIView.as_view(), name='gitprofile'),

    # path('article/', views.ArticleAPIView.as_view(), name="articles"),
    # path('article/<pk>', views.ArticleDetailAPIView.as_view(), name="article_detail"),

    # path('category/', views.CategoryAPIView.as_view(), name="category"),
    # path('category/<pk>', views.CategoryDetailAPIView.as_view(), name="category_detail"),

    # path('tag/', views.TagAPIView.as_view(), name="tag"),
    # path('tag/<pk>', views.TagDetailAPIView.as_view(), name="tag_detail"),

    # path('user/', views.UserAPIView.as_view(), name='users'),
    # path('user/<pk>', views.UserDetailAPIView.as_view(), name='user_detail'),
]