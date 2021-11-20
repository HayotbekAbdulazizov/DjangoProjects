# Generated by Django 3.2.5 on 2021-08-02 19:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]