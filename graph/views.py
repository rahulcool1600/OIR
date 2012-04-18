from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template.loader import render_to_string
from requests.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator

def index(request):
	#if request.user.is_authenticated:
	#login(request, request.user)
	return render_to_response('analytics.html')

def users(request):
	return HttpResponse(render_to_string('visitors.xml'))
