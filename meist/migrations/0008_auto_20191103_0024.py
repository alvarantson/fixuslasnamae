# Generated by Django 2.1.3 on 2019-11-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meist', '0007_auto_20190415_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.TextField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='e_mail',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='letter',
            field=models.TextField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='nimi',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='tel_nr',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='contact_us',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='email',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='header',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='name',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='phone',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='send',
            field=models.CharField(blank=True, max_length=99999),
        ),
        migrations.AlterField(
            model_name='meist_lang',
            name='your_problem',
            field=models.CharField(blank=True, max_length=99999),
        ),
    ]
