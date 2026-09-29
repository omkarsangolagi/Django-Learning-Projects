from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def add(request):
    a = int(input("enter the number:"))
    b =  int(input("enter the second number:"))
    c = a+b
    return HttpResponse(str(c))

def sub(request):
    d = int(input("enter the number:"))
    e =  int(input("enter the second number:"))
    f = d-e
    return HttpResponse(str(f))
def mul(request):
    d = int(input("enter the number:"))
    e =  int(input("enter the second number:"))
    f = d*e
    return HttpResponse(str(f))

def div(request):
    d = int(input("enter the number:"))
    e =  int(input("enter the second number:"))
    f = d/e
    return HttpResponse(str(f))

