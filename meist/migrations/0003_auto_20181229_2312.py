# Generated by Django 2.1.3 on 2018-12-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meist', '0002_aboutlang_contactform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='aboutlang',
        ),
        migrations.RemoveField(
            model_name='meist_lang',
            name='h1',
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kaardil',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kaardil2',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt2',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt_mail',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt_nimi',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt_sisu',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='kontakt_tel',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='meist',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AddField(
            model_name='meist_lang',
            name='saada',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='e_mail',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='letter',
            field=models.TextField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='nimi',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='tel_nr',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='lang',
            field=models.CharField(max_length=99999, unique=True),
        ),
    ]
