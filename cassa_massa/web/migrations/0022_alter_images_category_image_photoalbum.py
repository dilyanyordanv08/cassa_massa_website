# Generated by Django 4.0.3 on 2022-04-27 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles'),
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.images')),
            ],
        ),
    ]