# Generated by Django 2.1.3 on 2019-04-15 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0011_toode_esilehele'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toode',
            name='protsent',
        ),
    ]
