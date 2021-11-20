from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


## Category class
class Category(models.Model):
    name = models.CharField('name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books',on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('name', max_length=200, blank=True)
    price = models.PositiveIntegerField('price')
    old_price = models.PositiveIntegerField('old price', blank=True, null=True)
    image = models.ImageField('Book image', upload_to='Book_images/', blank=True, null=True)
    author = models.CharField('author', max_length=200, blank=True)
    published = models.DateField('Year of Publish', )
    file = models.FileField('Book itself', upload_to='book_files')
    instock = models.PositiveIntegerField('Num', default=0, blank=True)
    description = models.TextField('Extra Data', blank=True)

    def __str__(self):
        return self.name