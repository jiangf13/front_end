from django.db import models


# Create your models here.
class People(models.Model): 
    Male = True
    Female = False
    GENDERS= (
   (Male, 'Male'),
   (Female, 'Female')
)
    name = models.CharField(max_length=50) 
    age = models.IntegerField(default='0')
    gender = models.BooleanField(choices=GENDERS, null=True)
    people_Main_Img = models.ImageField(upload_to='images/') 