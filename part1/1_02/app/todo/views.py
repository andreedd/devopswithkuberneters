from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


# Create your views here.

def home(request):
    return HttpResponse(f"Server started in port {settings.PORT}")