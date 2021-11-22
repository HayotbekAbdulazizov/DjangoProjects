from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField('name', max_length=1000, blank=True)
    video = models.FileField('video',  upload_to='videos/')

    def __str__(self):
        return self.title