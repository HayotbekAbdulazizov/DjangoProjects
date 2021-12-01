# Generated by Django 3.2.4 on 2021-07-06 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='user_images/', verbose_name='Rasmi')),
                ('birthday', models.DateField(verbose_name='T. sanasi')),
                ('phone', models.PositiveIntegerField(default=0, verbose_name='Telefon')),
                ('address', models.CharField(max_length=250, verbose_name='Manzili')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]