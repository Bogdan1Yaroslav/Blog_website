# Generated by Django 2.2 on 2022-04-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_my_blog', '0006_auto_20220424_2120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='Image',
        ),
    ]