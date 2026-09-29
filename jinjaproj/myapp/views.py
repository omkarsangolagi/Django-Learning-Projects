from django.shortcuts import render

# Create your views here.

def view1(request):
    name = "rama"
    place = "bangalore"
    ctx = {'Name':name , 'Place':place}
    return render(request,'my.html',ctx)
