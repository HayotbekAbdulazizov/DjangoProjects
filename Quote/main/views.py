from django.shortcuts import render
from .models import Tags, Quote
# Create your views here.

def HomePage(request):
    quote = Quote.objects.all().order_by('?')[:1]
    context = {
        'quotes':quote
    }
    return render(request, 'index.html', context)