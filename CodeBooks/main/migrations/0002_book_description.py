# Generated by Django 3.2.5 on 2021-07-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, verbose_name='Extra Data'),
        ),
    ]
