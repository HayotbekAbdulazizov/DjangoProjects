from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# class HomePageView(TemplateView):
    # template_name = "index_pjax.html"




def pj1(request):
    return render(request, 'index_pjax.html')


def pj2(request):
    return render(request, 'index_pjax2.html')