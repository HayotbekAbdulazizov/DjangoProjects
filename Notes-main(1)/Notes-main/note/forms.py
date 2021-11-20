from django import forms
from .models import Notes

class AddNotesForm(forms.ModelForm):

	class Meta:
		model = Notes 
		fields = '__all__'
		exclude = ['star']


class UpdateNotesForm(forms.ModelForm):

	class Meta:
		model = Notes 
		fields = '__all__'
		exclude = ['star']
		widgets = {
			'body':forms.Textarea(attrs={'rows':30,'cols':8})
		}