from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from myapp.models import Student

# Create your views here.

class StudentList(ListView):
    model=Student 
    #default templates : student_list.html
    #default context : student_list

class StudentDetail(DetailView):
    model = Student

class StudentUpdate(UpdateView):
    model = Student
    fields = "__all__"

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student')
    #success url for display the target page
    #default template : student_confirm_delete.html

class StudentCreate(CreateView):
    model = Student
    fields = "__all__"
    #default template : student_form.html
    #default cntext : form

