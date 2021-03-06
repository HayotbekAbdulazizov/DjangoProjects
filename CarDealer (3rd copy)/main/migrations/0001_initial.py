# Generated by Django 3.2.2 on 2021-07-10 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brand')),
                ('brand_image', models.ImageField(blank=True, upload_to='brand_images/', verbose_name='Brand Image')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=75, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('max_tezlik', models.CharField(blank=True, max_length=10, verbose_name='Maximum Tezlik')),
                ('mileage', models.CharField(blank=True, max_length=100, verbose_name=' Mileage ')),
                ('image_main', models.ImageField(upload_to='posters/', verbose_name='ImageMain')),
                ('extra_data', models.TextField(blank=True, verbose_name='Extra Data')),
                ('price', models.CharField(blank=True, max_length=20, verbose_name='Narxi')),
                ('old_price', models.CharField(blank=True, max_length=30, verbose_name='Eski Narxi')),
                ('color', models.CharField(blank=True, choices=[('white', 'WHITE'), ('black', 'BLACK'), ('blue', 'BLUE'), ('green', 'GREEN'), ('yellow', 'YELLOW'), ('red', 'RED'), ('tomato', 'TOMATO'), ('pink', 'PINK'), ('teal', 'TEAL'), ('brown', 'BROWN')], max_length=50, verbose_name='Rangi')),
                ('fuel', models.CharField(blank=True, choices=[('diesel', 'DIESEL'), ('gas', 'GAS'), ('electric', 'ELECTRIC')], max_length=100, verbose_name='Fuel')),
                ('status', models.CharField(blank=True, choices=[('used', 'USED'), ('new', 'NEW')], max_length=50, verbose_name='USED or NEW')),
                ('power', models.CharField(blank=True, max_length=20, verbose_name='Power HP')),
                ('num_of_seats', models.CharField(blank=True, max_length=100, verbose_name='Orindiqlar soni')),
                ('yukxona_sigimi', models.CharField(max_length=50, verbose_name='Yukxona-Sigimi')),
                ('xavfsizlik', models.CharField(max_length=50, verbose_name='Xavfsizlik')),
                ('yonilgi_istemoli', models.CharField(max_length=50, verbose_name='Yonilgi-Istemoli')),
                ('xavfsizlik_yostiqchalari', models.CharField(max_length=50, verbose_name='Xavfsizlik-Yostiqchalari')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='main.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='*')),
                ('image', models.ImageField(blank=True, upload_to='posters/', verbose_name='Poster')),
                ('body', models.TextField(verbose_name='Body')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('num_of_comments', models.PositiveIntegerField(blank=True, default=0, verbose_name='Comments')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='main.brand')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='News Images')),
                ('news', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_images', to='main.news')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ismingiz')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Mavzu')),
                ('message', models.TextField(verbose_name='Xabar matni')),
                ('commented', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Bildirilgan sana')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.news')),
            ],
            options={
                'verbose_name': 'Muhokama',
                'verbose_name_plural': 'Muhokamalar',
            },
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/', verbose_name='Car Images')),
                ('car', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='main.car')),
            ],
            options={
                'verbose_name': 'Tovar rasmlari',
                'verbose_name_plural': 'Tovar rasmlari',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='main.category'),
        ),
    ]
