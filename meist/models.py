from django.db import models

# Create your models here.
class meist_lang(models.Model):
	lang = models.CharField(max_length=99999, unique=True)
	header = models.CharField(max_length=99999, blank=True)
	contact_us = models.CharField(max_length=99999, blank=True)
	name = models.CharField(max_length=99999, blank=True)
	phone = models.CharField(max_length=99999, blank=True)
	email = models.CharField(max_length=99999, blank=True)
	your_problem = models.CharField(max_length=99999, blank=True)
	send = models.CharField(max_length=99999, blank=True)
	def __str__(self):
		return self.lang

class contactform(models.Model):
	nimi = models.CharField(max_length=99999, blank=True)
	tel_nr = models.CharField(max_length=99999, blank=True)
	e_mail = models.CharField(max_length=99999, blank=True)
	letter = models.TextField(max_length=99999, blank=True)
	date = models.TextField(max_length=99999, blank=True)
	def __str__(self):
		return self.nimi + ' - ' +self.tel_nr + ' - ' +self.e_mail + ' - ' +self.date