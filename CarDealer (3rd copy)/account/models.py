from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,
		on_delete=models.CASCADE,
		related_name='user_profile')
	avatar = models.ImageField('Rasmi',upload_to='user_images/', blank=True, null=True, default='profile_img/default.jpg')
	birthday = models.CharField('T. sanasi', max_length=50, blank=True)
	phone = models.PositiveIntegerField('Telefon', default=0,blank=True,null=True)
	address = models.CharField('Manzili', max_length=250,blank=True,null=True)

	def __str__(self):
		return f"Foydalanuvchi - {self.user.username}"