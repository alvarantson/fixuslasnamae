from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import repair_lang, menu
from statistika.views import collect_statistics
# Create your views here.
def repair(request):
	collect_statistics(request, "repair")
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/repair') #INDEX\i puhul '/'
	
	menuu = []
	hetkel = ""
	asd = []
	for i in menu.objects.filter(lang=request.session['lang']):
		asd.append(i)
	asd = sorted(asd, key=lambda k: k.item_cat) 
	for i in asd:
		if hetkel != i.item_cat:
			hetkel = i.item_cat
			menuu.append({"item_cat":"KATEGOORIA","item_name":hetkel,"item_price":""})
		menuu.append(i)


	return render(request, 'repair.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang': repair_lang.objects.get(lang=request.session['lang']),
		'menu': menuu,
		'social_media':social_media.objects.all()
		})