# Generated by Django 3.2.16 on 2022-10-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221008_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='food_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'rice'), (2, 'bread and rotis'), (3, 'meat'), (4, 'fish'), (5, 'drinks'), (6, 'sweet'), (7, 'seafood'), (8, 'vegetarian')], null=True),
        ),
    ]
