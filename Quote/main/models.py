from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField('name',max_length=30)
    slug = models.SlugField('*')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Quote(models.Model):
    Tags = models.ManyToManyField(Tags)
    slug = models.SlugField('*')
    title = models.CharField('title',max_length=100)
    body = models.TextField('body', blank=True)
    author = models.CharField('Author', max_length=100, blank=True)
    author_image = models.ImageField('Author Image', blank=True, upload_to='Author_Images/')
    published = models.DateTimeField('time', auto_now_add=True)

    def __str__(self):
        return self.title