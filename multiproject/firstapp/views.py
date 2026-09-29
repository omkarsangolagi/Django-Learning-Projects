from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):

    a = "this is the response from the first app"

    return HttpResponse(a)

