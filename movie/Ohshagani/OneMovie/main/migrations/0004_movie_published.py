# Generated by Django 3.2.5 on 2021-07-30 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_movie_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Published'),
            preserve_default=False,
        ),
    ]
