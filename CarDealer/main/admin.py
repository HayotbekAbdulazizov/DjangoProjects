from django.contrib import admin
from .models import Brand, Category, News, Car, CarImages, NewsImages, Comment, CarouselImages
# Register your models here.

# admin.site.register(Colors)


class CarImageAdmin(admin.StackedInline):
	model = CarImages

class NewsImageAdmin(admin.StackedInline):
	model =  NewsImages

class CarCarouselImageAdmin(admin.StackedInline):
	model =  CarouselImages

@admin.register(Brand)
class ProAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', ]
	list_display_links = ['name', ]

	class Meta:
		model = Brand

@admin.register(Category)
class ProAdmin(admin.ModelAdmin):
	list_display = ['name', 'id', ]
	list_display_links = ['name', ]

	class Meta:
		model = Car


@admin.register(Car)
class ProAdmin(admin.ModelAdmin):
	inlines = [CarImageAdmin, CarCarouselImageAdmin]
	list_display = ['image_main','model', 'category', ]
	list_display_links = ['model', ]
	prepopulated_fields = {'slug':('model',)}

	class Meta:
		model = Car

@admin.register(News)
class ProAdmin(admin.ModelAdmin):
	inlines = [NewsImageAdmin]
	list_display = ['image','title', 'category', ]
	list_display_links = ['title', ]
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = News
