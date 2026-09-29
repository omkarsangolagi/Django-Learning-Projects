from django.contrib import admin
from myapp.models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','email','job','salary']

admin.site.register(Employee,EmployeeAdmin)