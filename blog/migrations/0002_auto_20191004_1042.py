# Generated by Django 2.1.4 on 2019-10-04 02:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='context',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
