# Generated by Django 4.0.3 on 2022-04-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_photoalbum'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]