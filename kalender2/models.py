# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class google_link(models.Model):
	link = models.CharField(max_length=999)