# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class statistics_entry(models.Model):
	datetime = models.DateTimeField("Aeg", auto_now_add=True)
	appname = models.CharField("Rakenduse nimi", max_length=99)
	referer = models.CharField("Mis rakendusest tuli", max_length=999, blank=True)
	session_key = models.CharField("Sessiooni võti", max_length=9999)
	def __str__(self):
		return str(self.datetime)+" - "+self.appname+" -from: "+self.referer