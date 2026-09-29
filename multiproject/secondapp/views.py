from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.

def second(request):

    a = "this is the response from the second app"

    return HttpResponse(a)

