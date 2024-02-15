# Generated by Django 5.0.1 on 2024-02-15 07:30

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Authorname', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn10', models.CharField(max_length=255, unique=True)),
                ('title', models.TextField()),
                ('thumbnail', models.URLField(blank=True)),
                ('upload', models.ImageField(blank=True, upload_to='uploads/')),
                ('description', models.TextField()),
                ('published_year', models.IntegerField(null=True)),
                ('average_rating', models.FloatField(null=True)),
                ('num_pages', models.IntegerField(null=True)),
                ('ratings_count', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField()),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='Book.author')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='Book.category')),
            ],
        ),
        migrations.CreateModel(
            name='MyRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingno', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_products', to='Book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
