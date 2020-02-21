from django.db import models

# Create your models here.
class varuosad_entry(models.Model):
	nr = models.CharField(max_length=999)
	nimi = models.CharField(max_length=999)
	kontakt = models.CharField(max_length=999)
	automark = models.CharField(max_length=999)
	varuosade_kood = models.CharField(max_length=999)
	nimetus = models.CharField(max_length=999)
	hind = models.CharField(max_length=999)
	kogus = models.CharField(max_length=999)
	tellitud_kuup = models.CharField(max_length=999)
	saabus_kuup = models.CharField(max_length=999)
	valja_kuup = models.CharField(max_length=999)
	ettemaks = models.CharField(max_length=999)
	aeg = models.CharField(max_length=999)
	kes_tegi = models.CharField(max_length=999)

	def __str__(self):
		return self.nr +' - '+self.nimi+' - '+self.aeg+' - '+self.kes_tegi

		
class google_link(models.Model):
	link = models.CharField(max_length=999)