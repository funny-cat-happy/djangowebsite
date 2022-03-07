# Generated by Django 3.0.4 on 2021-06-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthManage', '0002_userinftable'),
    ]

    operations = [
        migrations.CreateModel(
            name='muteuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qqnumber', models.CharField(max_length=20, unique=True)),
                ('qqmessage1', models.TextField(null=True)),
                ('qqmessage2', models.TextField(null=True)),
                ('qqmessage3', models.TextField(null=True)),
                ('qqmessagetimes', models.IntegerField(default=0)),
                ('lastmessagedate', models.DateTimeField()),
            ],
            options={
                'db_table': 'muteuser',
            },
        ),
    ]
