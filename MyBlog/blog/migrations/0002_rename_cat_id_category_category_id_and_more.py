# Generated by Django 4.1.1 on 2022-09-22 07:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='cat',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]