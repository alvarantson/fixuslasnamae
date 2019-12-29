from django.shortcuts import render
from login.models import worker
from .forms import UploadFileForm
from .XML_TXT02 import *
from django.http import HttpResponse, Http404
# Create your views here.

def xmltotxt(request):
	try:
		request.session['kalender_priority'] = worker.objects.get(name=request.session['worker']).kalender_priority
		request.session['varuosad_priority'] = worker.objects.get(name=request.session['worker']).varuosad_priority
		request.session['tookoda_priority'] = worker.objects.get(name=request.session['worker']).tookoda_priority
	except:
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		file_data = writeTXT(ImportXML(request.FILES["file"]), request.POST["name"])
		response = HttpResponse(file_data, content_type='application/text charset=utf-8')
		response['Content-Disposition'] = 'attachment; filename="{}.txt"'.format(request.POST["name"])
		return response
	else:
		form = UploadFileForm()

	return render(request, 'xmltotxt.html', {'form': form})
