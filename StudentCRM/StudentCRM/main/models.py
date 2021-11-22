from django.db import models

# Create your models here.

class Cource(models.Model):
    name = models.CharField('Nomi',max_length=300, blank=True)
    slug = models.SlugField('*', unique=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    status = (
        ('Keldi', 'Keldi'),
        ('Kelmad', 'Kelmadi'),
        ('Aniqmas', 'Aniqmas'),
    )
    name = models.CharField('Ismi', max_length=300, blank=True)
    cource = models.ForeignKey(Cource, related_name='students',on_delete=models.CASCADE , blank=True, null=True)
    phone = models.PositiveIntegerField('Telefon Raqami', default=+998,blank=True)
    age = models.PositiveIntegerField('Yoshi', default=0, blank=True)
    status = models.CharField('Status', max_length=50, choices=status, blank=True)
    comment = models.TextField('Comment', blank=True)
    date = models.DateTimeField('Sana', auto_now_add=True)

    def __str__(self):
        return self.name