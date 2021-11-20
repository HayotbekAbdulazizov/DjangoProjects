# Generated by Django 3.2.5 on 2021-07-26 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=200, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(default=datetime.datetime(2021, 7, 26, 13, 48, 18, 818005, tzinfo=utc), verbose_name='Year of Publish'),
            preserve_default=False,
        ),
    ]
