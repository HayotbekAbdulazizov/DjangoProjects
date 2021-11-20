from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Rubrics)
class RubricAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','year','country']
    prepopulated_fields = {'slug':('title',)}