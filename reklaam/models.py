from django.db import models

# Create your models here.
class reklaam_entry(models.Model):
	nimi = models.CharField(max_length=99999)
	img = models.ImageField()
	def __str__(self):
		return self.nimi
