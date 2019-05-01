from django.db import models

# Create your models here.
class browser_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	h1 = models.CharField(max_length=999)
	saadavausPoes = models.CharField(max_length=999, default="")
	vanaHind = models.CharField(max_length=999, default="")
	uusHind = models.CharField(max_length=999, default="")
	kaibeMaks = models.CharField(max_length=999, default="")
	enne = models.CharField(max_length=999, default="")
	def __str__(self):
		return self.lang

class toode(models.Model):
	lang = models.CharField(max_length=3, default='')
	name = models.CharField(max_length=999, default='')
	price = models.CharField(max_length=9, default='')
	prevprice = models.CharField(max_length=9, default='')
	description = models.TextField(default='')
	esilehele = models.CharField('esilehele y/n', max_length=1, default='n')
	img = models.ImageField()
	def __str__(self):
		if  self.esilehele == 'y':
			return 'Esilehel: ' + self.lang+' - '+self.name
		else:
			return self.lang+' - '+self.name
		