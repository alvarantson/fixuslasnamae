from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs, ad, social_media
from .models import meist_lang, contactform
import datetime
from django.core.mail import send_mail
from statistika.views import collect_statistics
# Create your views here.
def meist(request):
	collect_statistics(request, "meist")
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/meist') #INDEX\i puhul '/'

		if request.POST['submit-btn'] == 'contact':
			new = contactform.objects.create(
				nimi=request.POST['name'],
				tel_nr=request.POST['phone'],
				e_mail=request.POST['email'],
				letter=request.POST['letter'],
				date=str(datetime.datetime.now().time())
				)
			send_mail(
				"Fixus Lasnamae Kiri: "+request.POST["name"]+" - "+str(datetime.datetime.now().time()),
				request.POST["name"]+"\n"+request.POST["phone"]+"\n"+request.POST["email"]+"\n"+str(datetime.datetime.now().time())+"\n"+request.POST["letter"]+"\n",
				request.POST["email"],["alvarantson@gmail.com"]
				)
	ad2 = []
	for nr in range(len(ad.objects.all())):
		ad2.append(nr)
	return render(request, 'meist.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'lang':meist_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'ads':ad.objects.all(),
		'ads2':ad2,
		'social_media':social_media.objects.all()
		})