from os import name
from django.db import models
from django.db.models.fields import SlugField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField('Category Name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Tag Name', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)

    def __str__(self):
        return self.name


class Point(models.Model):
    title = models.TextField('Title')
    category = models.ForeignKey(Category, related_name='points', on_delete=models.CASCADE ,blank=True, null=True)
    author = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField('*', blank=True, null=True)
    image = models.ImageField('Image', upload_to='images/')
    like = models.PositiveIntegerField('Like Count', default=0, )
    dislike = models.PositiveIntegerField('DisLike Count', default=0, )
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')
    published = models.DateTimeField('Published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
     

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField('image', upload_to='user_images/', blank=True)
    name = models.CharField('name', blank=True, null=True, max_length=300   )
    liked_posts = models.ManyToManyField(Point, related_name='user_liked_posts')
    

    def __str__(self):
        return str(self.user) 



class Comment(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField("Ismingiz", max_length=50)
    email = models.EmailField("Email", max_length=250, blank=True)
    message = models.TextField("Xabar matni",)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name='Comment'
        verbose_name_plural='Comments'