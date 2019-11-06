from django.db import models

# Create your models here.
class index_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	eelmine = models.CharField(max_length=99999, blank=True)
	jargmine = models.CharField(max_length=99999, blank=True)
	uuri_lahemalt = models.CharField(max_length=99999, blank=True)
	sooduspakkumised = models.CharField(max_length=99999, blank=True)
	vaata_koiki_pakkumisi = models.CharField(max_length=99999, blank=True)
	enne = models.CharField(max_length=99999, blank=True)
	uuri_lahemalt = models.CharField(max_length=99999, blank=True)
	def __str__(self):
		return self.lang

class index_icon(models.Model):
	lang = models.CharField(max_length=3)
	logo = models.CharField(max_length=999, blank=True)
	header = models.CharField(max_length=999, blank=True)
	link = models.CharField(max_length=999, blank=True)
	text = models.TextField(blank=True)
	def __str__(self):
		return self.lang+' - '+self.header+' - logod saab siit glyphicon- jargne: https://getbootstrap.com/docs/3.3/components/'