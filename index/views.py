from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import index_lang, index_icon
from browser.models import toode
# Create your views here.
def index(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/') #INDEX\i puhul '/'
	ad2 = []
	for nr in range(len(ad.objects.all())):
		ad2.append(nr)

	return render(request, 'index.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang':index_lang.objects.get(lang=request.session['lang']),
		'icons':index_icon.objects.filter(lang=request.session['lang']),
		'tooted': toode.objects.filter(lang=request.session['lang'], esilehele='y'),
		'ads':ad.objects.all(),
		'ads2':ad2,
		'social_media': social_media.objects.all()
		})