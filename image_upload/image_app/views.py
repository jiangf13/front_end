
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .something import *
  
# Create your views here. 
def people_image_view(request): 
  
    if request.method == 'POST': 
        form = PeopleForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            name=request.POST.get('name','')
            age=request.POST.get('age','')
            gender=request.POST.get('gender','')
            people_Main_Img_url=request.POST.get('people_Main_Img.url','')
            tmp(name)
            tmp(age)
            tmp(gender)
            tmp('done')
            return redirect('success') 
    else: 
        form = PeopleForm() 
    return render(request, 'image_app/people_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
    return redirect('display_people_images') 


def display_people_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of people. 
        Peoples = People.objects.all()  
        return render(request, 'image_app/display_people_images.html', 
                     {'people_images' : Peoples})