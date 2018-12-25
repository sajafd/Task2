# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def home(request):
	
	response_dict = {
	"member 1" : "Fatma",
	"member 2" : "Saja"
	}

	return JsonResponse(response_dict)