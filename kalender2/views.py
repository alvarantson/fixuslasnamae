from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import google_link
from login.models import worker
from login.views import is_worker
# Create your views here.
def kalender2(request):
	is_worker(request)

	return render(request, 'kalender.html', context={
		'link':google_link.objects.first()
		})