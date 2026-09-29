from django.shortcuts import render
from .mock_data import PRODUCTS

# Create your views here.
def home_view(request):
    context={
        "products":PRODUCTS
    }
    return render(request,'home.html',context)

def details_view(request,id):
    context = {}
    for product in PRODUCTS:
        if product['id']==id:
            context['product']=product 
            break
    return render(request,'details.html',context)

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')
