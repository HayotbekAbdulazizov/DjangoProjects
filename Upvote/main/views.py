from django.shortcuts import redirect, render
from .models import Category, Point, Profile
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import *
from django.views.generic import CreateView
from .context_pro import view_all

# obj, created = Person.objects.get_or_create(
    # first_name='John',
    # last_name='Lennon',
    # defaults={'birthday': date(1940, 10, 9)},
# )


# Create your views here.
def homePage(request):
    points = Point.objects.all()

    context = {
        'points':points,
    }
    return render(request, 'index.html', context)


class CreatePointView(CreateView):
    model = Point
    template_name = "create_point.html"
    fields = ['title', 'category', 'author','tags']
    success_url = '/'



def addLike(request, point_id):
    point = Point.objects.get(id=point_id)
    point.like += 1
    
    point.save()

    
    return redirect('main:home')

def disLike(request, point_id):
    user = User.objects.get(id=request.user.id)
    point = Point.objects.get(id=point_id)
    if user in point.like.all():
        point.like.remove(user)
    if user in point.dislike.all():
        point.dislike.remove(user)
    else:
        point.dislike.add(user)            
    point.save()    
    return redirect('main:home')



def pointDetails(request, point_id):
    point = Point.objects.get(id=point_id)
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.point = point
            if request.user.username:
                user = User.objects.get(id=request.user.id)
                f.name = user.username  
                if user.email:
                    f.email = user.email
            f.save()
    else:
        form = AddCommentForm()
    
    context = {
    'point':point,
    'form':form
    }
    return render(request, 'point_details.html', context)


def profilePage(request):
    context = {
        'profile':Profile.objects.get_or_create(user=request.user)
    }
    return render(request,'profile.html', context)







