from django.shortcuts import render
from login.models import worker
from .forms import UploadFileForm
from .conv import *
from django.http import HttpResponse, Http404
from login.views import is_worker
# Create your views here.

def xmltotxt(request):
	is_worker(request)
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		inquiry = import_motoral(request.FILES["file"])
		doc = export_baltiautoosad(inquiry)

#		file_data = writeTXT(ImportXML(), request.POST["name"])
		response = HttpResponse(doc.toxml(encoding="utf-8"), content_type='application/text charset=utf-8')
		response['Content-Disposition'] = 'attachment; filename="{}.xml"'.format(request.POST["name"])
		return response
	else:
		form = UploadFileForm()

	return render(request, 'xmltotxt.html', {'form': form})
