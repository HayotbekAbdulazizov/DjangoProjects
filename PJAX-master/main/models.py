from doctest import debug_script
from django.db import models

# Create your models here.
class GitProfile(models.Model):
    username = models.CharField("Username", max_length=300)
    pat = models.CharField("PAT0", max_length=300)
    full_name = models.CharField('Full Name', max_length=300, blank=True)
    email = models.EmailField('email', max_length=200,blank=True)
    password = models.CharField('password', max_length=200,blank=True)  
    description = models.TextField("Description", blank=True)
    status = models.BooleanField('Commit Status', default=True)
    
    def __str__(self):
        return self.username

    def repos_count(self):
        return self.repos.count()


class Repository(models.Model):
    profile = models.ForeignKey(GitProfile, on_delete=models.CASCADE, related_name='repos')
    name = models.CharField('Name', max_length=300)
    description = models.TextField('Text', blank=True)
    
    def __str__(self):
        return self.name