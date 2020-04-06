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

	apps = statistics_entry.objects.order_by().values('appname').distinct()
#	keys = statistics_entry.objects.order_by().values('session_key').distinct()
	stats = statistics_entry.objects.all()

	site_referals = []
	# [ {appname, referers[appname, occurance]} ]
	
	for app in apps:
		item = {"appname":app["appname"], "referers":[]}
		for i in apps:
			if i != app:
				item["referers"].append([i["appname"],0])
		site_referals.append(item)



	site_views = []
	# [ {appname, count} ]

	for app in apps:
		site_views.append({"appname":app["appname"], "count":0})

#	site_keys = []

	# KINDOF POINTLESS
#	for key in keys:
#		site_views.append({"key":key["session_key"], "road":[]})

	#filling
	for entry in stats:
		for i in range(len(site_views)):
			#print(site_views[i]["appname"], entry.appname)
			#print(site_views[i]["appname"] == entry.appname)
			if site_views[i]["appname"] == entry.appname:
				site_views[i]["count"] += 1

		for i in range(len(site_referals)):
			if site_referals[i]["appname"] == entry.appname:
				for j in range(len(site_referals[i]["referers"])):
					print(site_referals[i]["referers"][j][0] , entry.referer)
					if site_referals[i]["referers"][j][0] == entry.referer:
						site_referals[i]["referers"][j][1] += 1

	site_views = sorted(site_views, key=lambda k: k['count'])[::-1]

	for i in range(len(site_views)):
		site_views[i]["block_height"] = float(25)*(float(site_views[i]["count"])/float(site_views[0]["count"]))

	for i in range(len(site_referals)):
		site_referals[i]["referers"] = sorted(site_referals[i]["referers"], key=lambda k: k[1])[::-1]
		for j in range(len(site_referals[i]["referers"])):
			site_referals[i]["referers"][j].append(float(25)*(float(site_referals[i]["referers"][j][1])/float(float(site_views[0]["count"]))))

	return render(request, "statistics.html", context={"site_referals": site_referals, "site_views": site_views, "app_count": len(site_views)})

def collect_statistics(request, current_app):
	try:
		print("Not logged in stats, worker: "+request.session["worker"])
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
			print("Not logged in stats, user: "+request.user.username)