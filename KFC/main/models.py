from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


## Category class
class Category(models.Model):
    name = models.CharField('name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True)
    image = models.ImageField('image', upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name



class Food(models.Model):
    category = models.ForeignKey(Category, related_name='foods',on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('name', max_length=200, blank=True)
    price = models.PositiveIntegerField('price')
    old_price = models.PositiveIntegerField('old price', blank=True, null=True)
    image = models.ImageField('food image', upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.name