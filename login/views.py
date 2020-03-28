from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import worker
from meist.models import contactform
from django.contrib.auth.models import User

# Create your views here.
def login(request):
	if bool(request.POST) == True:
		if request.POST['submit-btn'] == 'login':
			if str(worker.objects.filter(name=request.POST['name'],password=request.POST['password'])) != '<QuerySet []>':
				request.session['worker'] = request.POST['name']
				request.session['kalender_priority'] = worker.objects.get(name=request.POST['name']).kalender_priority
				request.session['varuosad_priority'] = worker.objects.get(name=request.POST['name']).varuosad_priority
				request.session['tookoda_priority'] = worker.objects.get(name=request.POST['name']).tookoda_priority
				return HttpResponseRedirect('/login') #INDEX\i puhul '/'
			else:
				return HttpResponse('<a href="/login">vale parool/kasutajanimi</a>')
		if request.POST['submit-btn'] == 'logout':
			del request.session['worker']
			return HttpResponseRedirect('/login') #INDEX\i puhul '/'
	if request.user.is_superuser:
		request.session['worker'] = "admin"
	try:
		return render(request,'login-hub.html',context={"mails":contactform.objects.all(), "workers":worker.objects.all(), "superusers":User.objects.all()})
	except:
		pass

	if request.user.is_superuser:
		request.session['worker'] = 'admin'
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'

	return render(request, 'login.html', context={})