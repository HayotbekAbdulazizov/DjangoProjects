from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/<slug:slug>',
    	views.ProductDetailView.as_view(),
    	name='detail'),
    path('category/detail/<pk>',
    	views.CategoryDetailView.as_view(),
    	name='category_detail'
    	),
		path('search/', views.movieSearch, name='search'),
		# path('cart/', views.cartPage, name='cart'),


#      path('send/',views.send_mails, name='user_send_mail')
]