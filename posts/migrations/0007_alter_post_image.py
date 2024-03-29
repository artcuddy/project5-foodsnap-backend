# Generated by Django 3.2.16 on 2023-01-22 11:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='../default-placeholder_m2h1kl', force_format='JPEG', keep_meta=True, quality=90, scale=None, size=[622, 622], upload_to='images/'),
        ),
    ]
