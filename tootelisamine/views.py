# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from navbar.models import langs
from browser.models import toode
from login.views import is_worker

from google.cloud import translate

import random
import string
# Create your views here.
def lang_to_code(input_lang):
	for item in [["est","et"],["rus","ru"],["eng","en"],["fin","fi"]]:
		if input_lang == item[0]:
			input_lang = item[1]
			break
	return input_lang

def tolgi(tekst, alg_keel, lopp_keel):
	client = translate.TranslationServiceClient()

	project_id = "fixus-lasnamae-1555334564252"
	parent = client.location_path(project_id, "global")

	response = client.translate_text(
		parent = parent,
		contents=tekst,
		mime_type="text/plain",
		source_language_code=lang_to_code(alg_keel),
		target_language_code=lang_to_code(lopp_keel))
	valjund = []
	for translation in response.translations:
		valjund.append(translation.translated_text)
	return valjund

def randomString(stringLength=100):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def tootelisamine(request):
	notice = ""
	is_worker(request)
	if request.POST:

		# IF USING TRANSLATE
#		try: 
		test = request.POST["translate"]
		main = request.POST["main"]
		toode_id = randomString()
		picture = request.FILES["image"]
		try:
			esilehele = request.POST["esilehele"]
			esilehele = "y"
		except:
			esilehele = "n"
		for lang in langs.objects.all():
			price = request.POST[main+"_price"]
			prevprice = request.POST[main+"_prevprice"]
			if main == lang.lang:
				name = request.POST[main+"_name"]
				description = request.POST[main+"_description"]
			else:
				tekst = [request.POST[main+"_name"],request.POST[main+"_description"]]
				sisu = tolgi(tekst, main, lang.lang)
				name = sisu[0]
				description = sisu[1]
			toode.objects.create(toode_id= toode_id, lang=lang.lang, name=name, price=price, prevprice=prevprice, description=description, esilehele=esilehele, img=picture)
		notice = "Toode edukalt lisatud ja tõlgitud!"
#		except:
#			notice = "Toote lisamine ja tõlkimine EBAÕNNESTUS!"

		# IF NOT TRANSLATING
		try: 
			test = request.POST["translate"]
		except:
			picture = request.FILES["image"]
			toode_id = randomString()
			try:
				esilehele = request.POST["esilehele"]
				esilehele = "y"
			except:
				esilehele = "n"
			for lang in langs.objects.all():
				name = request.POST[lang.lang+"_name"]
				price = request.POST[lang.lang+"_price"]
				prevprice = request.POST[lang.lang+"_prevprice"]
				description = request.POST[lang.lang+"_description"]
				toode.objects.create(toode_id= toode_id, lang=lang.lang, name=name, price=price, prevprice=prevprice, description=description, esilehele=esilehele, img=picture)
				notice = "Toode lisatud edukalt!"
	return render(request, "tootelisamine.html", context={"langs":langs.objects.all(), "lang_separator": float(99)/float(len(langs.objects.all())), "notice":notice})