from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from django.urls import reverse

# Create your models here.


class Brand(models.Model):
	name = models.CharField('Brand', max_length=100,)
	brand_image = models.ImageField('Brand Image', upload_to='brand_images/', blank=True)

	def __str__(self):
		return f"{self.name}"


class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    slug = models.SlugField('*', max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"




## ALL news related to all categories
class News(models.Model):
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('*', max_length=100, unique=True)
    category = models.ForeignKey(Brand, on_delete=CASCADE, related_name='news', blank=True, null=True)
    image = models.ImageField('Poster', upload_to='posters/', blank=True)
    body = models.TextField('Body')
    published = models.DateTimeField(auto_now_add=True, blank=True)
    num_of_comments = models.PositiveIntegerField('Comments', default=0, blank=True)

    def __str__(self):
	    return f"{self.title}"


## Cars car models
class Car(models.Model):
	COLORS=(
	('white','WHITE'),
	('black','BLACK'),
	('blue','BLUE'),
	('green','GREEN'),
	('yellow','YELLOW'),
	('red','RED'),
	('tomato','TOMATO'),
	('pink','PINK'),
	('teal','TEAL'),
	('brown','BROWN'),
	)

	FUELS = (
		('diesel','DIESEL'),
		('gas','GAS'),
		('electric','ELECTRIC')
	)

	USED = (
		('used','USED'),
		('new','NEW')
	)

	model = models.CharField('Name', max_length=75)
	slug = models.SlugField('*', max_length=100, unique=True)
	category = models.ForeignKey(Category, on_delete=CASCADE, related_name='cars', blank=True, null=True)
	brand = models.ForeignKey(Brand, on_delete=CASCADE, related_name='cars', blank=True, null=True)
	full_name = models.CharField('Full Name', max_length=100)
	max_tezlik = models.CharField('Maximum Tezlik', max_length=10, blank=True)
	mileage = models.CharField(' Mileage ', max_length=100, blank=True)
	image_main = models.ImageField('ImageMain', upload_to='posters/')      
	extra_data = models.TextField('Extra Data', blank=True)
	price = models.PositiveIntegerField('Price')
	old_price = models.PositiveIntegerField('Old Price')
	color = models.CharField('Rangi', max_length=50, choices=COLORS, blank=True)
	fuel = models.CharField('Fuel', max_length=100, choices=FUELS, blank=True)
	status = models.CharField('USED or NEW', max_length=50, choices=USED, blank=True)
	power = models.CharField('Power HP', max_length=20, blank=True)
	num_of_seats = models.CharField('Orindiqlar soni', max_length=100 ,blank=True)
	yukxona_sigimi = models.CharField('Yukxona-Sigimi' ,max_length=50)
	xavfsizlik = models.CharField('Xavfsizlik' ,max_length=50)
	yonilgi_istemoli = models.CharField('Yonilgi-Istemoli' ,max_length=50)
	xavfsizlik_yostiqchalari = models.CharField('Xavfsizlik-Yostiqchalari', max_length=50)
	published = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return f"{self.model}"



class CarImages(models.Model):
	car = models.ForeignKey(Car,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='car_images')
	image = models.ImageField('Car Images',
		upload_to='car_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.car.model

	class Meta:
		verbose_name = 'Tovar rasmlari'
		verbose_name_plural = 'Tovar rasmlari'



class CarouselImages(models.Model):
	car = 	car = models.ForeignKey(Car,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='car_carousel_images')
	image = models.ImageField('Carousel Image', upload_to='carousel_car_img/')



class NewsImages(models.Model):
	news = models.ForeignKey(News,
		default=None,
		null=True,
		blank=True,
		on_delete=models.CASCADE,
		related_name='news_images')
	image = models.ImageField('News Images',
		upload_to='news_images/',
		blank=True, null=True,)

	def __str__(self):
		return self.news.title





class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField("Ismingiz", max_length=50)
    email = models.EmailField("Email", max_length=250)
    subject = models.CharField("Mavzu", max_length=100)
    message = models.TextField("Xabar matni")
    commented = models.DateTimeField( 'Bildirilgan sana' ,  auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name='Muhokama'
        verbose_name_plural='Muhokamalar'



