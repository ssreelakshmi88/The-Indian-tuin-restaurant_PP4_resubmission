# Generated by Django 3.2.16 on 2022-10-15 20:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('food_type', models.PositiveIntegerField(choices=[(1, 'starter'), (2, 'main'), (3, 'dessert')], null=True)),
            ],
        ),
    ]
