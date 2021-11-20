from django.shortcuts import render,redirect
from .forms import UserRegistrationForm

from django.views.generic import DetailView, UpdateView
from .models import Profile
from django.contrib.auth import logout
# Create your views here.

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
		    # Create a new user object but avoid saving it yet
		    new_user = user_form.save(commit=False)
		    # Set the chosen password
		    new_user.set_password(user_form.cleaned_data['password'])
		    # Save the User object
		    new_user.save()
		    # Save the new user Profile object
		    Profile.objects.create(user=new_user)
		    return redirect('account:login')
	else:
		user_form = UserRegistrationForm()
	return render(request,'registration/register.html', {'form':user_form})


def logout_view(request):
    logout(request)
    return redirect('account:login')


class UserProfileView(DetailView):
	model = Profile
	template_name = 'registration/profile.html'


class UpdateUserProfileView(UpdateView):
	model = Profile
	fields = ['avatar','birthday','phone','address']
	success_url = '/'
