# Generated by Django 4.0.3 on 2022-04-16 08:18

import cassa_massa.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=35, validators=[cassa_massa.web.validators.validate_only_letters_and_spaces]),
        ),
    ]
