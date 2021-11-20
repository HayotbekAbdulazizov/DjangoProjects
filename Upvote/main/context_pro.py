from django.contrib.auth.models import User
from .models import Category, Profile
from django.contrib.auth.models import User


def view_all(request):
    # profiles = Profile.objects.get_or_create(user=request.user)
    
    # for user in profiles:
        # print(user)

    context = {
        # 'profiles   ':profiles,
    }
    return context