# Generated by Django 2.2 on 2022-04-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_my_blog', '0003_delete_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_images',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотографии'),
        ),
    ]
