# Generated by Django 5.0.2 on 2024-03-04 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='photo',
            new_name='image',
        ),
    ]
