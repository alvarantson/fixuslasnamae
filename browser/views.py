from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import browser_lang
from .models import toode
from statistika.views import collect_statistics
from navbar.views import linker
# Create your views here.
def browser(request):
	try:
		return linker(request)
	except:
		pass
	collect_statistics(request, "browser")
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/browser') #INDEX\i puhul '/'
	ad2 = []
	for nr in range(len(ad.objects.all())):
		ad2.append(nr)
	return render(request, 'browser.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'tooted': toode.objects.filter(lang=request.session['lang']),
		'lang': browser_lang.objects.get(lang=request.session['lang']),
		'ads':ad.objects.all(),
		'ads2':ad2,
		'social_media':social_media.objects.all()
		})