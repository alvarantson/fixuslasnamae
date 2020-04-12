# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import statistics_entry
# Create your views here.
def statistika(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/admin")

	# TRY IF NOTHING TO RETURN
	try: 
		date1 = "2000-01-01"
		date2 = "2300-01-01"
		if request.POST:
			date1 = request.POST["date1"]
			date2 = request.POST["date2"]

		apps = statistics_entry.objects.order_by().values('appname').distinct()
		stats = statistics_entry.objects.filter(datetime__range=[date1,date2])

		site_referals = []
		# [ {appname, referers[appname, occurance]} ]
		
		for app in apps:
			item = {"appname":app["appname"], "referers":[]}
			for i in apps:
				if i != app:
					item["referers"].append([i["appname"],0])
			site_referals.append(item)

		site_views = []
		for app in apps:
			site_views.append({"appname":app["appname"], "count":0})

		#filling
		for entry in stats:
			for i in range(len(site_views)):
				if site_views[i]["appname"] == entry.appname:
					site_views[i]["count"] += 1

			for i in range(len(site_referals)):
				if site_referals[i]["appname"] == entry.appname:
					for j in range(len(site_referals[i]["referers"])):
						if site_referals[i]["referers"][j][0] == entry.referer:
							site_referals[i]["referers"][j][1] += 1

		site_views = sorted(site_views, key=lambda k: k['count'])[::-1]

		for i in range(len(site_views)):
			site_views[i]["block_height"] = float(25)*(float(site_views[i]["count"])/float(site_views[0]["count"]))

		for i in range(len(site_referals)):
			site_referals[i]["referers"] = sorted(site_referals[i]["referers"], key=lambda k: k[1])[::-1]
			for j in range(len(site_referals[i]["referers"])):
				site_referals[i]["referers"][j].append(float(25)*(float(site_referals[i]["referers"][j][1])/float(float(site_views[0]["count"]))))
	except:
		site_referals = []
		site_views = []
	return render(request, "statistics.html", context={"site_referals": site_referals, "site_views": site_views, "app_count": len(site_views), "date1": date1, "date2":date2})



def collect_statistics(request, current_app):
	try:
		print("Visit not logged in stats, logged in as worker: "+request.session["worker"])
	except:
		if not request.user.is_authenticated:
			if not request.session.session_key:
				request.session.create()
			session_key = request.session.session_key
			try: 
				prev_app = request.META['HTTP_REFERER'].split("/")[len(request.META['HTTP_REFERER'].split("/"))-1]
			except:
				prev_app = "-"
			
			statistics_entry.objects.create(appname=current_app, session_key=session_key, referer=prev_app)
		else:
			print("Visit not logged in stats, logged in as user: "+request.user.username)