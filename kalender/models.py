from django.db import models

# Create your models here.
class kalender_entry(models.Model):
	nimi = models.CharField(max_length=999)
	paev = models.CharField(max_length=999)
	tundide_arv = models.CharField(max_length=999)
	kes_tegi = models.CharField(max_length=999)


class google_link(models.Model):
	link = models.CharField(max_length=999)