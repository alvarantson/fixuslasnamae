# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-02 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='statistics_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Aeg')),
                ('appname', models.CharField(max_length=99, verbose_name='Rakenduse nimi')),
                ('referer', models.CharField(blank=True, max_length=999, verbose_name='Mis rakendusest tuli')),
                ('session_key', models.CharField(max_length=9999, verbose_name='Sessiooni v\xf5ti')),
            ],
        ),
    ]