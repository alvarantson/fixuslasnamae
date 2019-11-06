from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from login.models import worker
from repair.models import menu as repair_menu
# Create your views here.
def lister(text):
	listing = []
	text = text.replace("\r","")
	for i in text.split("\n"):
		listing.append(i.split("\t"))
	for i in range(len(listing)): # no empty rows
		if listing[i] == [""]:
			listing.remove(listing[i])
	return listing

def loader(request):
	try:
		request.session['kalender_priority'] = worker.objects.get(name=request.session['worker']).kalender_priority
		request.session['varuosad_priority'] = worker.objects.get(name=request.session['worker']).varuosad_priority
		request.session['tookoda_priority'] = worker.objects.get(name=request.session['worker']).tookoda_priority
	except:
		return HttpResponseRedirect('/login') #INDEX\i puhul '/'

	if request.POST:
		items = lister(request.POST["sisu"])
		if request.POST["table"] == "repair":
			if request.POST["delete"] == "yes":
				repair_menu.objects.filter(lang=items[0][0]).delete()
			for item in items:
				repair_menu.objects.create(lang=item[0], item_cat=item[1], item_name=item[2], item_price=item[3])


	return render(request, 'loader.html', context={
		
		})