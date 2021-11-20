from main.models import Tags
from django.contrib import admin
from .models import Tags, Quote

# Register your models here.
@admin.register(Tags)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Quote)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title','author', 'id']
	list_display_links = ['title','author', 'id']
	prepopulated_fields = {'slug':('title',)}

