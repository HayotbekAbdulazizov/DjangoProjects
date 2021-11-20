from django.shortcuts import render
from django.urls.conf import path
from .models import *
from django.views.generic import TemplateView


class AllGadgetsView(TemplateView):
    template_name = "index.html"



