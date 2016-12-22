from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import DustBin
from .dustbinlogic import match
def check_cookie(request):
	flag = False
	if 'last_location' in request.session:
		li = request.session.get('last_location')
		flag = True
		return flag
	else:
		return flag
def home(request):
	flag = check_cookie(request)
	return render_to_response("index.html",{"flag":flag})


def check(request):
	lat = request.GET.get('lat',"")
	lon = request.GET.get("long","")
	if lat and lon:
		data = [str(lat),str(lon)]
		request.session['last_location'] = data
		print 'SESSION SET!'
		return HttpResponseRedirect("/")
	else:
		return HttpResponse("VALUE NOT PROVIDED")

def claim(request):
	dustbin = return_matching_dustbin(request)

	if dustbin:
		return render_to_response("success.html",{"coord":dustbin})



def return_matching_dustbin(request):
	every =  DustBin.objects.all()
	data = request.session.get("last_location")
	data = [float(i) for i in data]
	tocheck = []
	for i in every:
		tocheck.append([float(i.lat),float(i.lon)])

	print tocheck
	print data

	nearme = 0

	for i in (tocheck):
		if data == i:
			return i
		else:
			if match.is_near(data[0], i[0]):
				if match.is_near(data[1], i[1]):
					continue





def show_dustbin_count(request):
	every =  DustBin.objects.all()
	data = request.session.get("last_location")
	data = [float(i) for i in data]
	tocheck = []
	for i in every:
		tocheck.append([float(i.lat),float(i.lon)])

	print tocheck
	print data

	nearme = 0

	for i in (tocheck):
		if data == i:
			nearme+=1
		else:
			if match.is_near(data[0], i[0]):
				if match.is_near(data[1], i[1]):
					nearme+=1
	return HttpResponse(str(nearme))
