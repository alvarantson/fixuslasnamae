from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import google_link
from login.models import worker
from login.views import is_worker
# Create your views here.
def kalender2(request):
	is_worker(request)


#	if bool(request.POST) == True:

#		if 'remove' in request.POST['submit-btn']:
#			kalender_entry.objects.get(
#				nimi=request.POST['submit-btn'].split('~')[1],
#				paev=request.POST['submit-btn'].split('~')[2]
#			).delete()

#		if 'new' in request.POST['submit-btn']:
#			if len(kalender_entry.objects.filter(nimi=request.POST['nimi'].replace(' ','_'), paev=request.POST['paev'])) != 0:
#				return HttpResponse('<h2>Sellel paeval on juba sissekanne olemas! <a href="/kalender">Mine tagasi!</a></h2>')
#			kalender_entry.objects.create(
#				nimi = request.POST['nimi'].replace(' ','_'),
#				paev = request.POST['paev'],
#				tundide_arv = request.POST['tundide_arv'],
#				kes_tegi = request.POST['kes_tegi']
#			)

#		if 'edit' in request.POST['submit-btn']:
#			edit = kalender_entry.objects.get(nimi=request.POST['nimi'], paev=request.POST['paev'])
#			edit.nimi = request.POST['nimi']
#			edit.paev = request.POST['paev']
#			edit.tundide_arv = request.POST['tundide_arv']
#			edit.kes_tegi = request.POST['kes_tegi']
#			edit.save()

#		return HttpResponseRedirect('/kalender')

	return render(request, 'kalender.html', context={
#		'items':kalender_entry.objects.all().reverse()
		'link':google_link.objects.first()
		})