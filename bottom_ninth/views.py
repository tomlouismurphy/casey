from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def gamestatus(request):
	return HttpResponse('It is the bottom of the ninth. The Giants lead 3-2, Madison Bumgarner is pitching, and Eric Hosmer, Billy Butler and Alex Gordon are due up.')