# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def home(request):
	
	response_list = ["Fatma", "Saja"]

	return JsonResponse(response_list, safe=False)