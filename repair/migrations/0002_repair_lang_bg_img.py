# Generated by Django 2.1.3 on 2019-11-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair_lang',
            name='bg_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
