# Generated by Django 2.1.3 on 2018-11-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='browser_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=3, unique=True)),
                ('h1', models.CharField(max_length=999)),
            ],
        ),
    ]
