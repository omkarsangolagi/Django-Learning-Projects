from django import forms
from myapp.models import *
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='all'
    def clean_name(self):
        n=self.cleaned_data["name"]
        if len(n)<=3:
            raise forms.ValidationError("min no of characters must be greater than or equal to 4")
        return n
    
    def clean_age(self):
        a=self.cleaned_data["age"]
        if a<=0:
            raise forms.ValidationError("age is always positive ")
        return a