# Generated by Django 3.0.4 on 2021-06-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinformation',
            name='FirstImageName',
            field=models.CharField(default='无', max_length=10),
        ),
        migrations.AlterField(
            model_name='goodsinformation',
            name='SecondImageName',
            field=models.CharField(default='无', max_length=10),
        ),
        migrations.AlterField(
            model_name='goodsinformation',
            name='ThirdImageName',
            field=models.CharField(default='无', max_length=10),
        ),
    ]
