from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
	)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.

from django.conf import settings
from django.core.mail import send_mail


# 1. TemplateView
# 2. ListView
# 3. DetailView
# 4. View
class CategoryDetailView(DetailView):
	model = Category
	# template_name = ''
	
	
class HomePageView(LoginRequiredMixin,ListView):
	login_url = '/account/login/'
	model = Product
	paginate_by = 4
	template_name = 'index.html'
	context_object_name = 'products' # object_list


class ProductDetailView(DetailView):
	model = Product


# @login_required
def send_mails(request):
	user = request.user
	subject = 'welcome to GFG world'
	message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
	email_from = settings.EMAIL_HOST_USER
	sending = send_mail( subject, message, email_from, [user.email])
	if sending:
		return HttpResponse('Done')




import json
def movieSearch(request):
    data = {}
    query = request.GET.get('data')
    movies = list(Product.objects.filter(slug__icontains=query).values())
    data['data'] = movies
    return JsonResponse(data)


# def cartPage(request, )