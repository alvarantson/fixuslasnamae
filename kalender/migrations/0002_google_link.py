# Generated by Django 2.1.3 on 2019-11-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='google_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=999)),
            ],
        ),
    ]
