# Generated by Django 2.2 on 2022-04-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_my_blog', '0004_post_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_images',
            field=models.ImageField(blank=True, null=True, upload_to='files/', verbose_name='Фотографии'),
        ),
    ]