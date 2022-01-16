from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import google_link
from login.models import worker
from login.views import is_worker
# Create your views here.
def hooldus(request):
	is_worker(request)
	
	return render(request, 'kalender.html', context={
		'link':google_link.objects.get(name="hooldus")
		})


def rehvivahetus(request):
	is_worker(request)
	
	return render(request, 'kalender.html', context={
		'link':google_link.objects.get(name="rehvivahetus")
		})


def rehvihotell(request):
	is_worker(request)
	
	return render(request, 'kalender.html', context={
		'link':google_link.objects.get(name="rehvihotell")
		})