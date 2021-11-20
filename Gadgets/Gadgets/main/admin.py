from django.contrib import admin
from .models import Category, Tag, Gadget
from django.utils.html import mark_safe

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'id', 'published']
	list_display_links = ['title', 'id']
	prepopulated_fields = {'slug':('title',)}
    # readonly_fiels = ('get_image',)

    # def get_image(self, obj):
        # return mark_safe(f"<")





