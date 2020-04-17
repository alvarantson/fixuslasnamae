from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import google_link
# Create your views here.
def kokkuvote(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/login")

	return render(request, 'kalender.html', context={
		'link':google_link.objects.first()
		})