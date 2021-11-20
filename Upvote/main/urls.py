from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('create/', views.CreatePointView.as_view(), name='create_point'),
    path('addlike/<int:point_id>', views.addLike, name='addlike'),
    path('dislike/<int:point_id>', views.disLike, name='dislike'),
    path('details/<int:point_id>', views.pointDetails, name='point_details'),
    path('profile/', views.profilePage, name='profile'),



]