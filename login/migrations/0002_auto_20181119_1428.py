# Generated by Django 2.1.3 on 2018-11-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='kalender_priority',
            field=models.CharField(choices=[('K', 'kirjutamine'), ('V', 'vaatamine'), ('M', 'midagi')], default='', max_length=999),
        ),
        migrations.AddField(
            model_name='worker',
            name='tookoda_priority',
            field=models.CharField(choices=[('K', 'kirjutamine'), ('V', 'vaatamine'), ('M', 'midagi')], default='', max_length=999),
        ),
        migrations.AddField(
            model_name='worker',
            name='varuosad_priority',
            field=models.CharField(choices=[('K', 'kirjutamine'), ('V', 'vaatamine'), ('M', 'midagi')], default='', max_length=999),
        ),
    ]
