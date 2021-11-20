from .models import Student, Cource
from django.db import models
from django.shortcuts import redirect, render
from datetime import date
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
# Create your views here.




class HomePageView(TemplateView):
    template_name = 'index.html'