# Generated by Django 2.1.3 on 2018-11-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meist', '0002_auto_20181126_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='meist_lang',
            name='msg',
            field=models.CharField(default='', max_length=999),
        ),
    ]
