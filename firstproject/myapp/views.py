from django.shortcuts import render
from django.http import HttpResponse

# def view1(request):
#     a = "welcome to the django session......"
#     return HttpResponse(a)

def one(request):
    a = "starting the django project"

    return HttpResponse(a)


