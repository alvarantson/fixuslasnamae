# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.shortcuts import render

from browser.models import toode
from navbar.models import langs
from login.views import is_worker


# Create your views here.
def tootehaldus(request):
	is_worker(request)
	notice = ""
	keeled = langs.objects.all()
	if request.POST:
		# DELETE A TOODE
		if "delete" in request.POST["submit-btn"]:
			for item in toode.objects.filter(toode_id=request.POST["submit-btn"].split("_")[0]):
				item.delete()
				notice = "Toode: "+request.POST["submit-btn"].split("_")[0]+" edukalt eemaldatud!"
		# NUKE TOODE
		elif "nuke" in request.POST["submit-btn"]:
			for item in toode.objects.all():
				item.delete()
				notice = "Kõik tooted edukalt eemaldatud!"
		# EDIT TOODE
		elif "edit" in request.POST["submit-btn"]:
			ID = request.POST["submit-btn"].split("_")[0]
			try:
				img = request.FILES["image"]
			except:
				img = toode.objects.filter(toode_id=ID)[0].img
			price = request.POST["price"]
			prevprice = request.POST["prevprice"]
			esilehele = request.POST["esilehele"]
			for keel in keeled:
				lang = keel.lang
				name = request.POST[keel.lang+"_name"]
				description = request.POST[keel.lang+"_description"]
				toode.objects.get(lang=keel.lang,toode_id=ID).delete()
				toode.objects.create(toode_id= ID, lang=keel.lang, name=name, price=price, prevprice=prevprice, description=description, esilehele=esilehele, img=img)
			notice = "Toode: "+ID+" edukalt muudetud!"

	toote_id = toode.objects.all().values("toode_id").distinct()
	tooted = []
	for ID in toote_id:
		item = []
		for lang in keeled:
			item.append(toode.objects.get(lang=lang.lang, toode_id=ID["toode_id"]))
		tooted.append(item)

	
	
	return render(request, "tootehaldus.html", context={"tooted":tooted, "lang_separator": float(99)/float(len(langs.objects.all())), "notice":notice})