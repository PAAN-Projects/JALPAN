# Generated by Django 4.1.3 on 2023-01-12 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_food_food_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]