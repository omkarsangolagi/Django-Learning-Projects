from django.shortcuts import render
from myapp.models import Student

def fakeview(request):
    s = Student.objects.all()
    d = {'stud': s}
    return render(request, 'fake.html', d)