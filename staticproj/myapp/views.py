from django.shortcuts import render

# Create your views here.

def myview(request):
    name = 'rama'
    animal = 'Rabbit'
    bird = 'peacock'
    ctx = {"Name":name,"Animal":animal,"Bird":bird}
    return render(request,'fav.html',ctx)