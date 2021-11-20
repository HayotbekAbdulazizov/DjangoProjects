from django.contrib import admin
from .models import Category, Book

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Book)
class FoodAdmin(admin.ModelAdmin):
	list_display = ['name','price','file', 'id']
	list_display_links = ['name','price','file']    