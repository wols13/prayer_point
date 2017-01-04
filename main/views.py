from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
	template = loader.render_to_string('main/headers.html', request)
	template += loader.render_to_string('main/index.html', request)
	return HttpResponse(template)
	
def sorted_by_scripture(request):
	template = loader.render_to_string('main/headers.html', request)
	return HttpResponse(template)

def sorted_by_category(request):
	template = loader.render_to_string('main/headers.html', request)
	return HttpResponse(template)
