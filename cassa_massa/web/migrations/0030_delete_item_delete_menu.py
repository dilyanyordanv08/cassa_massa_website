# Generated by Django 4.0.3 on 2022-04-27 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_menu_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]