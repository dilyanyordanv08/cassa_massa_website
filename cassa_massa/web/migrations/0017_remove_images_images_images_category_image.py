# Generated by Django 4.0.3 on 2022-04-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_rename_category_image_images_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='images',
        ),
        migrations.AddField(
            model_name='images',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
