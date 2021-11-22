from django.urls import path
from .import views

app_name = 'note'

urlpatterns = [
	path('', views.notes, name='notes'),
	path('delete/<int:note_id>', views.deleteNote, name='delete'),
	path('update/<pk>', views.UpdateNoteView.as_view(
		template_name='update.html'), name='update'),


	path('accounts/profile/', views.profile, name='profile')
]