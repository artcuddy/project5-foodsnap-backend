# Generated by Django 3.2.16 on 2022-12-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='content',
            new_name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='method',
            field=models.TextField(null=True),
        ),
    ]
