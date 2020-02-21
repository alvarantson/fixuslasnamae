from django.db import models

# Create your models here.
class tookoda_entry(models.Model):
	aeg = models.CharField(max_length=999)
	too_vottis_vastu = models.CharField(max_length=999)
	auto_mark = models.CharField(max_length=999)
	reg_nr = models.CharField(max_length=999)
	telefon = models.CharField(max_length=999)
	ettemaks = models.CharField(max_length=999)
	teostav_too = models.TextField()
	mured_kommentaarid = models.TextField()
	kes_tegi = models.CharField(max_length=999)

	
class google_link(models.Model):
	link = models.CharField(max_length=999)