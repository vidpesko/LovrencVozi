from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """Show homescreen"""
    return HttpResponse("Hello world")