# Generated by Django 3.2.16 on 2023-01-20 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_category_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]