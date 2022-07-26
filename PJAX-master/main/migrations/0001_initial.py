# Generated by Django 4.0.5 on 2022-06-11 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, verbose_name='Username')),
                ('pat', models.CharField(max_length=300, verbose_name='PAT0')),
                ('full_name', models.CharField(blank=True, max_length=300, verbose_name='Full Name')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='email')),
                ('password', models.CharField(blank=True, max_length=200, verbose_name='password')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Text')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repos', to='main.gitprofile')),
            ],
        ),
    ]
