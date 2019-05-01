from django.db import models

# Create your models here.
class meist_lang(models.Model):
	lang = models.CharField(max_length=99999, unique=True)
	header = models.CharField(max_length=99999, default='')
	contact_us = models.CharField(max_length=99999, default='')
	name = models.CharField(max_length=99999, default='')
	phone = models.CharField(max_length=99999, default='')
	email = models.CharField(max_length=99999, default='')
	your_problem = models.CharField(max_length=99999, default='')
	send = models.CharField(max_length=99999, default='')
	def __str__(self):
		return self.lang

class contactform(models.Model):
	nimi = models.CharField(max_length=99999, default='')
	tel_nr = models.CharField(max_length=99999, default='')
	e_mail = models.CharField(max_length=99999, default='')
	letter = models.TextField(max_length=99999, default='')
	date = models.TextField(max_length=99999, default='')
	def __str__(self):
		return self.nimi + ' - ' +self.tel_nr + ' - ' +self.e_mail + ' - ' +self.date