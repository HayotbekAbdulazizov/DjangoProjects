from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Notes(models.Model):
	COLORS = (
		('bg-warning','warning',),
		('bg-danger','danger',),
		('bg-primary','primary',),
		('bg-info','info',),
		('bg-success','success',),
		)
	title = models.CharField('Nomi', max_length=250)
	body = RichTextField()
	date = models.DateTimeField('Sana', auto_now_add=True)
	star = models.BooleanField('Yulduzi', default=False, null=True, blank=True)
	color = models.CharField('Rangi', max_length=50, choices=COLORS)

	def __str__(self):
		return self.title