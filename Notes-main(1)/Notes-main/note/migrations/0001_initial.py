# Generated by Django 3.2.4 on 2021-06-22 12:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Nomi')),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Sana')),
                ('star', models.BooleanField(default=False, verbose_name='Yulduzi')),
                ('color', models.CharField(choices=[('warning', 'bg-warning'), ('danger', 'bg-danger'), ('primary', 'bg-primary'), ('info', 'bg-info'), ('success', 'bg-success')], max_length=50, verbose_name='Rangi')),
            ],
        ),
    ]
