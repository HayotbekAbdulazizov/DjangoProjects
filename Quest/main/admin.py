from django.contrib import admin
from .models import Quest, Category, Tag
# Register your models here.

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
	list_display = ['title','category', 'id']
	list_display_links = ['title','category', 'id']
	prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name','id']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name','id']
	prepopulated_fields = {'slug':('name',)}