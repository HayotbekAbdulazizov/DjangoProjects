# Generated by Django 3.2.5 on 2021-07-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_carouselimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='old_price',
            field=models.PositiveIntegerField(verbose_name='Old Price'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
    ]
