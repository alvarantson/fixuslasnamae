from django.db import models

# Create your models here.
class repair_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	bg_img = models.ImageField(blank=True)
	header = models.CharField(max_length=999, blank=True)
	text = models.TextField(blank=True)
	menu = models.CharField(max_length=999, blank=True)
	table_field1 = models.CharField(max_length=99, blank=True)
	table_field2 = models.CharField(max_length=99, blank=True)
	def __str__(self):
		return self.lang


class menu(models.Model):
	lang = models.CharField(max_length=3)
	item_cat = models.CharField(max_length=99, blank=True)
	item_name = models.CharField(max_length=99, blank=True)
	item_price = models.CharField(max_length=9, blank=True)
	def __str__(self):
		return self.lang + " - " +self.item_cat + " - " +self.item_name
