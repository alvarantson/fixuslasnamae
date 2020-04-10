from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from navbar.models import contact, navbar_lang, langs
from .models import navbar_lang
from statistika.views import collect_statistics
# Create your views here.
def REPLACE(request):
	if 'lang' not in request.session:
		request.session['lang'] = 'est'
	flags = []
	for item in langs.objects.all():
		flags.append(item)
	if bool(request.POST) == True: 
		if request.POST['submit-btn'] == 'lang':
			request.session['lang'] = request.POST['langselect']
			return HttpResponseRedirect('/REPLACE') #INDEX\i puhul '/'
	return render(request, 'REPLACE.html', context={
		'contact':contact.objects.all()[0],
		'navbar_lang':navbar_lang.objects.get(lang=request.session['lang']),
		'flags':flags,
		'lang':REPLACE_lang.objects.get(lang=request.session['lang'])
		})

def linker(request):
	print(request.POST["submit-btn"].split("EXTERNAL")[1])
	if request.POST:
		if "EXTERNAL" in request.POST["submit-btn"]:
			url = request.POST["submit-btn"].split("EXTERNAL")[1]
			collect_statistics(request, url)
			return HttpResponseRedirect(url)
		else:
			raise EnvironmentError
	