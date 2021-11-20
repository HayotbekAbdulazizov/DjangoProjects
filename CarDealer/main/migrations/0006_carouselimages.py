# Generated by Django 3.2.5 on 2021-07-18 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_car_img/', verbose_name='Carousel Image')),
                ('car', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_carousel_images', to='main.car')),
            ],
        ),
    ]
