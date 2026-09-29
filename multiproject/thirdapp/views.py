from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.

def third(request):

    a = "this is the response from the third app"

    return HttpResponse(a)

