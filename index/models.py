from django.db import models

# Create your models here.
class index_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	eelmine = models.CharField(max_length=99999, default='')
	jargmine = models.CharField(max_length=99999, default='')
	uuri_lahemalt = models.CharField(max_length=99999, default='')
	sooduspakkumised = models.CharField(max_length=99999, default='')
	vaata_koiki_pakkumisi = models.CharField(max_length=99999, default='')
	enne = models.CharField(max_length=99999, default='')
	uuri_lahemalt = models.CharField(max_length=99999, default='')
	def __str__(self):
		return self.lang

class index_icon(models.Model):
	lang = models.CharField(max_length=3)
	logo = models.CharField(max_length=999)
	header = models.CharField(max_length=999, default='')
	text = models.TextField()
	def __str__(self):
		return self.lang+' - '+self.text+' - logod saab siit glyphicon- jargne: https://getbootstrap.com/docs/3.3/components/'