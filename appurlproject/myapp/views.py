from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    a = "django classes are started ......."
    return HttpResponse(a)
