from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('',views.AllGadgetsView.as_view(), name='home'),
]
