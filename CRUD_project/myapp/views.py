from django.shortcuts import render, redirect
from myapp.models import Student
from myapp.forms import StudentForm

# Create your views here.

def display(request):
    s = Student.objects.all()
    d = {'stud': s}
    return render(request, 'display.html', d)

def insert_view(request):
    f=StudentForm()
    if request.method == "POST":
        f = StudentForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/display/')        
    d = {'form': f}
    return render(request, 'form.html', d)

def update_view(request,id):
    s = Student.objects.get(id=id)
    f = StudentForm(instance=s)
    if request.method == "POST":
        f = StudentForm(request.POST, instance=s)
        if f.is_valid():
            f.save()
            return redirect('/display/')
    d = {'form': f}
    return render(request, 'form.html', d)
        

def delete_view(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('/display/')

