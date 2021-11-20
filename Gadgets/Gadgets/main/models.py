from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nomi', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Nomi', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)

    def __str__(self):
        return self.name


class Gadget(models.Model):
    title = models.CharField('Title', max_length=200, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    tag = models.ManyToManyField(Tag, related_name='tags')
    image = models.ImageField('Image', upload_to='gadgets_images/')
    published = models.DateTimeField('published', auto_now_add=True)
    file_format = models.CharField('Format', max_length=300, blank=True)
    description = models.TextField('Description',)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['published']    
        verbose_name_plural = 'Gadgets'