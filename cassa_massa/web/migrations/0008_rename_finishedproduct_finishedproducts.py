# Generated by Django 4.0.3 on 2022-04-17 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_finishedproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FinishedProduct',
            new_name='FinishedProducts',
        ),
    ]
