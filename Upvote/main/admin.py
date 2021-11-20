from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Comment,  Point, Profile, Tag
user = User.objects.get(id=1)
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name',]
	prepopulated_fields = {'slug':('name',)}

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'published', ]
	list_display_links = ['title',]
	prepopulated_fields = {'slug':('title',)}


@admin.register(Comment)
class PointAdmin(admin.ModelAdmin):
	list_display = ['point', 'name', 'id','email' ]
	list_display_links = ['point', 'name', 'id','email' ]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user' ]
	list_display_links = ['user' ]


