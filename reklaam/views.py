from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import reklaam_entry
from login.models import worker
# Create your views here.
def reklaam(request):
	request.session['paper'] = '-'
	try:
		request.session['kalender_priority'] = worker.objects.get(name=request.session['worker']).kalender_priority
		request.session['varuosad_priority'] = worker.objects.get(name=request.session['worker']).varuosad_priority
		request.session['tookoda_priority'] = worker.objects.get(name=request.session['worker']).tookoda_priority
	except:
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'

	items = reklaam_entry.objects.all()
	if bool(request.POST) == True:
		request.session['paper'] = request.POST['submit-btn']
		items = reklaam_entry.objects.filter(nimi=request.POST['submit-btn'])

	return render(request, 'reklaam.html', context={
		'items': items
		})