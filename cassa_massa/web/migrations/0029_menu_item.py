# Generated by Django 4.0.3 on 2022-04-27 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_remove_kategorianeshtosiimage_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.menu')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]