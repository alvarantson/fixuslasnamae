# Generated by Django 2.2.9 on 2020-04-10 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_worker_tolked_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='tolked_priority',
        ),
    ]