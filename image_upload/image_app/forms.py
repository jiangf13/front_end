from django import forms 
from .models import *
  
class PeopleForm(forms.ModelForm): 
  
    class Meta: 
        model = People 
        fields = ['name', 'age', 'gender', 'people_Main_Img']
