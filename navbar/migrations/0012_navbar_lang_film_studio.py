# Generated by Django 2.1.3 on 2019-11-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0011_auto_20191101_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar_lang',
            name='film_studio',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
