# Generated by Django 3.2.4 on 2021-07-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='other_colors',
        ),
        migrations.AddField(
            model_name='product',
            name='other_colors',
            field=models.ManyToManyField(related_name='other_colors', to='shop.Colors'),
        ),
    ]
