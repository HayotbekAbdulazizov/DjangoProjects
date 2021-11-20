from django.urls import path,reverse_lazy
from .import views

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import (
	PasswordChangeView,
	PasswordChangeDoneView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordResetConfirmView,
	PasswordResetCompleteView
	)


app_name = 'account'

urlpatterns = [
	# Passwords settings
	# Password Change
	path('password_change/', PasswordChangeView.as_view(
		template_name='registration/change_password.html',
		),name='password_change'),
	path('password_change/done/', PasswordChangeDoneView.as_view(
		template_name='registration/password_changed.html'),
		name='password_change_done'),


	# Password Reset
	path('password_reset/', PasswordResetView.as_view(
		template_name='registration/reset_password.html',
		email_template_name='registration/password_reset_email.html')
		, name="password_reset"),

	path('password_reset/done', PasswordResetDoneView.as_view(
		template_name='registration/email_sent.html',
		),
		name='password_reset_done'),

	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
		template_name="registration/confirm_password.html",),
		name="confirm_reset"),

	path('password/reset/done/', PasswordResetCompleteView.as_view(
		template_name="registration/password_confirmed.html"),
		name='password_reset_complete'),




    path('login/', LoginView.as_view(
    	redirect_authenticated_user=False,
    	),
    	name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<pk>', views.UserProfileView.as_view(), name='profile'),
    path('profile/update/<pk>', views.UpdateUserProfileView.as_view(), name='update_profile'),
]