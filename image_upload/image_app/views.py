
# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .something import *
from django.views import View

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from matplotlib.backends.backend_agg import FigureCanvasAgg

from PIL import Image
from io import BytesIO
import requests
import json
import cv2
import os


# Create your views here. 
def people_image_view(request): 
  
    if request.method == 'POST': 
        form = PeopleForm(request.POST, request.FILES) 
  
        if form.is_valid():
            # read image from POST, send to api and store the response locally
            image = request.FILES['people_Main_Img']
            if image:
                image_handler(image,request.POST.get('age',''),request.POST.get('name',''))
            
            name=request.POST.get('name','')
            age=request.POST.get('age','')
            gender=request.POST.get('gender','')
            people_Main_Img_url=request.POST.get('people_Main_Img.url','')

            form.save()
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



def image_handler(image,age,name):
    path=default_storage.save('images/lena.jpg', ContentFile(image.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT,path)
    img = cv2.imread(tmp_file)
    _, img_encoded = cv2.imencode('.jpg', img)
    
    addr = 'http://localhost:5000'
    test_url = addr + '/infer'


    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'file': content_type}

    print("########################")
    # save image locally
    with open(tmp_file, 'rb') as f:
        files = {'file':img_encoded.tostring()}
        response = requests.post(test_url, files=files, data={'age':age})#, headers=headers)
        i = Image.open(BytesIO(response.content))
        i.save("media/images/"+name+".png")
    print("########################")