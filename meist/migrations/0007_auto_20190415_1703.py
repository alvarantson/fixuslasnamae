# Generated by Django 2.1.3 on 2019-04-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meist', '0006_meist_lang_h1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meist_lang',
            name='h1',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kaardil',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kaardil2',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt2',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt_mail',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt_nimi',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt_sisu',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='kontakt_tel',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='meist',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='saada',
        ),
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.TextField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='contact_us',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='email',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='header',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='name',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='phone',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='send',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='your_problem',
            field=models.CharField(default='', max_length=99999),
        ),
    ]
