from django.shortcuts import render, redirect
from .models import Notes
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
# Create your views here.

from .forms import AddNotesForm, UpdateNotesForm

def notes(request):
	if request.method == 'POST':
	
		form = AddNotesForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		
		form = AddNotesForm()
	notes = Notes.objects.all()
	paginator = Paginator(notes, 1)  # Show 2 notes per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'add_form':form,
		'page_obj': page_obj
	
	}
	return render(request, 'notes.html', context)

def deleteNote(request, note_id):
	note = Notes.objects.get(id=note_id)
	note.delete()
	return redirect('note:notes')


class UpdateNoteView(UpdateView):
	model = Notes 
	fields = ['title','body','color']
	success_url = '/'


def profile(request):
	return render(request, 'account/profile.html')