from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
	resp = """
	<h1>HELLO HTML</h1>
	"""
	#return HttpResponse(resp)
	return render(request,"tickets/home.html")