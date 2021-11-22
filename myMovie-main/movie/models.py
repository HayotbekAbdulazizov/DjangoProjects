from django.db import models

# Create your models here.
class Rubrics(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = models.SlugField('*', max_length=200, unique=True)
    
    class Meta:
        verbose_name_plural = 'Rubrics'

    def __str__(self):
        return str(self.name)

class Genre(models.Model):
    name = models.CharField('Name', max_length=200)
    slug = models.SlugField('*', max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Genres'

    def __str__(self):
        return str(self.name)

    
class Movie(models.Model):
    title = models.CharField('Title', max_length=300)
    slug = models.SlugField('*', max_length=200, unique=True)
    rubric = models.ForeignKey(Rubrics,on_delete=models.CASCADE,related_name='rubric')
    genre = models.ManyToManyField('Genre', related_name='genres')
    poster = models.ImageField('Movie poster', upload_to='movie_posters/')
    description = models.TextField("Movie description",blank=True)
    director = models.CharField("Film director", max_length=100)
    actors = models.CharField('Film actors', max_length=200)
    year = models.PositiveIntegerField(default=0)
    country = models.CharField('Country', max_length=100)
    duration = models.CharField('Duration', max_length=100)
    like = models.PositiveIntegerField('Likes', default=0)
    dislike = models.PositiveIntegerField('DisLikes', default=0)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return str(self.title)


