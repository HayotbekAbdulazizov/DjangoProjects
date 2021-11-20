from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
	# add comment
	class Meta:
		model = Comment
		fields = '__all__' # hamma maydonini olish
		exclude = ['point','name','email'] # qaysi maydonlarni ko'rsatmaslik