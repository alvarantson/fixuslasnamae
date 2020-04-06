from django.db import models

# Create your models here.
class browser_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	header = models.CharField(max_length=999, blank=True)
	text = models.TextField( blank=True)
	h1 = models.CharField(max_length=999, blank=True)
	bg_img = models.ImageField(blank=True)
	saadavausPoes = models.CharField(max_length=999, blank=True)
	vanaHind = models.CharField(max_length=999, blank=True)
	uusHind = models.CharField(max_length=999, blank=True)
	kaibeMaks = models.CharField(max_length=999, blank=True)
	enne = models.CharField(max_length=999, blank=True)
	def __str__(self):
		return self.lang

class toode(models.Model):
	lang = models.CharField(max_length=3)
	toode_id = models.CharField(max_length=999, default="")
	name = models.CharField(max_length=999, blank=True)
	price = models.CharField(max_length=9, blank=True)
	prevprice = models.CharField(max_length=9, blank=True)
	description = models.TextField(blank=True)
	esilehele = models.CharField('esilehele y/n', max_length=1, default='n')
	img = models.ImageField(blank=True)
	def __str__(self):
		if  self.esilehele == 'y':
			return 'Esilehel: ' + self.lang+' - '+self.name
		else:
			return self.lang+' - '+self.name
		