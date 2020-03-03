from django.shortcuts import render
import multiprocessing
from django.http import HttpResponse

# Create your views here.
def users_view(req):
	data = "users"
	return HttpResponse(data)
def cpu_view(req):
	number_cpus = multiprocessing.cpu_count()
	
	return HttpResponse(number_cpus)

