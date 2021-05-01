from django.db import models

# Create your models here.
	
class google_link(models.Model):
	names = [("rehvivahetus","rehvivahetus"),("hooldus","hooldus")]

	name = models.CharField(max_length=999, choices=names, unique=True, blank=True)
	link = models.CharField(max_length=999, blank=True)

	def __str__(self):
		return self.name