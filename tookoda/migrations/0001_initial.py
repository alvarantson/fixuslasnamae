# Generated by Django 2.1.3 on 2018-11-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tookoda_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aeg', models.CharField(max_length=999)),
                ('too_vottis_vastu', models.CharField(max_length=999)),
                ('auto_mark', models.CharField(max_length=999)),
                ('reg_nr', models.CharField(max_length=999)),
                ('telefon', models.CharField(max_length=999)),
                ('ettemaks', models.CharField(max_length=999)),
                ('teostav_too', models.TextField()),
                ('mured_kommentaarid', models.TextField()),
                ('kes_tegi', models.CharField(max_length=999)),
            ],
        ),
    ]
