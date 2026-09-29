import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakecrud_project.settings')
django.setup()

from myapp.models import Student
from faker import Faker

f=Faker()
def populate(n):
    for i in range(n):
        fname = f.name()
        fage = f.random_int(min=18,max=80)
        femail = f.email()
        fplace = f.address()
        Student.objects.get_or_create(name=fname,age=fage,email=femail,place=fplace)
populate(20)