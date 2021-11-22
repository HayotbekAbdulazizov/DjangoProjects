from django.contrib import admin
from .models import  Cource, Student 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', 'cource', 'status', 'date']
	list_display_links = ['name', 'id']

    
@admin.register(Cource  )
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name', 'id']

    