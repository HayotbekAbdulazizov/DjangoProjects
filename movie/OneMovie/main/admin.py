from django.contrib import admin
from .models import Rubrics, Genre,Movie

# Register your models here.
@admin.register(Rubrics)
class RubricsAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_display_links = ['name','slug']
	prepopulated_fields = {'slug':('name',)}

        
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_display_links = ['name','slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['title','year', 'country']
	list_display_links = ['title','year']
	prepopulated_fields = {'slug':('title',)}
