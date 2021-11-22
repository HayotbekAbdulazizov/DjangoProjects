from typing import Tuple
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Rubrics(models.Model):
    name = models.CharField('Name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, max_length=200)

    def __str__(self):
        return str(self.name)

class Genre(models.Model):
    name = models.CharField('Name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, max_length=200)

    def __str__(self):
        return str(self.name)

class Movie(models.Model):
    title = models.CharField('Title', max_length=300, blank=True)
    slug = models.SlugField('*', unique=True, max_length=300)
    rubric = models.ForeignKey(Rubrics, on_delete=models.CASCADE, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    poster = models.ImageField('Image', upload_to='movie/', blank=True)
    movie = models.FileField('File', upload_to='movies', blank=True)
    description = models.TextField('Description', blank=True)
    director = models.CharField('Director', max_length=200,blank=True)
    actors = models.CharField('Actors ', max_length=300, blank=True)
    year = models.PositiveIntegerField('Year', default=0)
    country = models.CharField('Country', max_length=500, blank=True)
    genre = models.CharField('Genre', max_length=200, blank=True)
    duration = models.CharField('Duration', max_length=100)
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    published = models.DateTimeField('Published', auto_now_add=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.title)
    
  


class Comment(models.Model):
    name = models.CharField('Name', max_length=200, blank=True)
    email = models.EmailField('Email', max_length=300, blank=True)
    text = models.TextField('Text', blank=True)

    def __str__(self):
        return str(self.name)

  