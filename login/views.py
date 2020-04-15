from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import worker
from meist.models import contactform
from django.contrib.auth.models import User
# Create your views here.
def is_worker(request):
	try:
		request.session['kalender_priority'] = worker.objects.get(name=request.session['worker']).kalender_priority
		request.session['kalender2_priority'] = worker.objects.get(name=request.session['worker']).kalender2_priority
		request.session['varuosad_priority'] = worker.objects.get(name=request.session['worker']).varuosad_priority
		request.session['tookoda_priority'] = worker.objects.get(name=request.session['worker']).tookoda_priority
		request.session['tooted_priority'] = worker.objects.get(name=request.session['worker']).tooted_priority
		request.session['kirjad_priority'] = worker.objects.get(name=request.session['worker']).kirjad_priority
	except:
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'
	finally:
		if request.user.is_superuser:
			request.session['kalender_priority'] = "K"
			request.session['kalender2_priority'] = "K"
			request.session['varuosad_priority'] = "K"
			request.session['tookoda_priority'] = "K"
			request.session['tooted_priority'] = "K"
			request.session['kirjad_priority'] = "K"
			request.session["worker"] = "admin"


def login(request):
	notice = ""
	if request.POST:
		if request.POST['submit-btn'] == 'notes':
			note.objects.all()[0].delete()
			note.objects.create(note=request.POST["notes"])
		if request.POST['submit-btn'] == 'login':
			if str(worker.objects.filter(name=request.POST['name'],password=request.POST['password'])) != '<QuerySet []>':
				request.session['worker'] = request.POST['name']
				is_worker(request)
				return HttpResponseRedirect('/login') #INDEX\i puhul '/'
			else:
				notice = "vale parool"
		if request.POST['submit-btn'] == 'logout':
			del request.session['worker']
			return HttpResponseRedirect('/login') #INDEX\i puhul '/'
	is_worker(request)
	try:
		return render(request,'login-hub.html',context={"mails":contactform.objects.all()[::-1], "workers":worker.objects.all(), "superusers":User.objects.all(), "logged_in":request.session["worker"], "notes": note.objects.all()[0]})
	except Exception as e:
		notice = e

	return render(request, 'login.html', context={"notice":notice})