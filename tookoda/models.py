from django.db import models

# Create your models here.
	
class google_link(models.Model):
	link = models.CharField(max_length=999)