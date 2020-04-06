from django.db import models

class worker(models.Model):
	name = models.CharField(max_length=99, unique=True)
	password = models.CharField(max_length=99)
	choices = (
		('M','midagi'),
		('V','vaatamine'),
		('L','lisamine'),
		('K','muutmine'),
	)
	tookoda_priority = models.CharField(max_length=999, choices=choices, default='')
	varuosad_priority = models.CharField(max_length=999, choices=choices, default='')
	kalender_priority = models.CharField(max_length=999, choices=choices, default='')
	kalender2_priority = models.CharField(max_length=999, choices=choices, default='')
	tooted_priority = models.CharField(max_length=999, choices=choices, default='')
	kirjad_priority = models.CharField(max_length=999, choices=choices, default='')
	def __str__(self):
		return self.name