from os import name
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

## Tag Model
class Tag(models.Model):
    name = models.CharField('name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)

    def __str__(self):
        return self.name

## Category Model
class Category(models.Model):
    name = models.CharField('name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True)

    def __str__(self):
        return self.name

## Question Model
class Quest(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    title = RichTextField('title')
    slug = models.SlugField('*', unique=True)
    answer = models.TextField('Answer')

    def __str__(self):
        return self.title