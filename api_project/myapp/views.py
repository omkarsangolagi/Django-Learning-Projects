from django.shortcuts import render
from myapp.models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.
# class EmployeeDetails(View):
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#         emp_data = {'name':emp.name,'age':emp.age,'email':emp.email,'place':emp.place,'job':emp.job,'salary':emp.salary}
#         json_data = json.dumps(emp_data)
#         return HttpResponse(json_data,content_type='application/json')


# class EmployeeDetails(View):
#     def get(self,request,id,*args,**kwargs):
#         emp = Employee.objects.get(id=id)
#         json_data = serialize('json',[emp])
#         return HttpResponse(json_data,content_type='application/json')


class EmployeeDetails(View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.all()
        json_data = serialize('json',emp)
        return HttpResponse(json_data,content_type='application/json')