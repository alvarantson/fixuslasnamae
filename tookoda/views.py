from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import tookoda_entry
from login.models import worker
# Create your views here.
def tookoda(request):
	try:
		request.session['kalender_priority'] = worker.objects.get(name=request.session['worker']).kalender_priority
		request.session['varuosad_priority'] = worker.objects.get(name=request.session['worker']).varuosad_priority
		request.session['tookoda_priority'] = worker.objects.get(name=request.session['worker']).tookoda_priority
	except:
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'


	if bool(request.POST) == True:

		if 'remove' in request.POST['submit-btn']:
			tookoda_entry.objects.get(
				aeg=request.POST['submit-btn'].split('~')[1],
				too_vottis_vastu=request.POST['submit-btn'].split('~')[2]
			).delete()

		if 'new' in request.POST['submit-btn']:
			tookoda_entry.objects.create(
				aeg = request.POST['aeg'],
				too_vottis_vastu = request.POST['too_vottis_vastu'],
				auto_mark = request.POST['auto_mark'],
				reg_nr = request.POST['reg_nr'],
				telefon = request.POST['telefon'],
				ettemaks = request.POST['ettemaks'],
				teostav_too = request.POST['teostav_too'],
				mured_kommentaarid = request.POST['mured_kommentaarid'],
				kes_tegi = request.POST['kes_tegi']
			)

		if 'edit' in request.POST['submit-btn']:
			edit = tookoda_entry.objects.get(aeg=request.POST['aeg'], too_vottis_vastu=request.POST['too_vottis_vastu'])
			edit.auto_mark = request.POST['auto_mark']
			edit.reg_nr = request.POST['reg_nr']
			edit.telefon = request.POST['telefon']
			edit.ettemaks = request.POST['ettemaks']
			edit.teostav_too = request.POST['teostav_too']
			edit.mured_kommentaarid = request.POST['mured_kommentaarid']
			edit.kes_tegi = request.POST['kes_tegi']
			edit.save()

		return HttpResponseRedirect('/tookoda')

	return render(request, 'tookoda.html', context={
		'items':tookoda_entry.objects.all().reverse()
		})