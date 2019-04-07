
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
            #image=request.FILES.get('images') 
            image = request.FILES['people_Main_Img']
            #print(type(image))
            if image:
                #form.save()
                image_handler(image)
            
            
            #files = {'file': open('1.jpg', 'rb')}
            #r = request.Post.get(url, files=files)
            #print(r.text)
            name=request.POST.get('name','')
            age=request.POST.get('age','')
            gender=request.POST.get('gender','')
            people_Main_Img_url=request.POST.get('people_Main_Img.url','')
            #tmp(name)
            #tmp(age)
            #tmp(gender)
            #tmp(people_Main_Img_url)
            return redirect('success') 
    else: 
        form = PeopleForm()
    #print("asdfasdfa")
    return render(request, 'image_app/people_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 
    return redirect('display_people_images') 


def display_people_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of people. 
        Peoples = People.objects.all()  
        
        img = cv2.imread('lena.jpg')
        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', img)
        # send http request with image and receive response
        response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

        print(json.loads(response.text))
        return render(request, 'image_app/display_people_images.html', 
                     {'people_images' : Peoples})



def image_handler(image):
    path=default_storage.save('images/lena.jpg', ContentFile(image.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT,path)
    #print("asdfkjasldkfja")
    img = cv2.imread(tmp_file)
    _, img_encoded = cv2.imencode('.jpg', img)
    
    addr = 'http://localhost:5000'
    test_url = addr + '/infer'


    # prepare headers for http request
    content_type = 'image/jpeg'
    headers = {'file': content_type}
    #print()
    #print()
    #print(img_encoded.tostring())
    #print()
    #print()
    #print("hahasdfsdf")
    print("########################")
    with open(tmp_file, 'rb') as f:
        files = {'file':img_encoded.tostring()}
        response = requests.post(test_url, files=files, headers=headers)
        i = Image.open(BytesIO(response.content))
        i.show()
        #, data=img_encoded.tostring()
        #, files=files
    #path=default_storage.save('json/tmp.json', ContentFile(json.loads(response.text)))
    

    #with open('tmp.json','w') as f:
        #print(response.files)
        #f.writelines(response.text)
    #with open('tmp.html','r') as f:
    print("########################")
    #print(tmp_file)
    os.remove(tmp_file)
    #print(type(json.loads(response.text)))
    #print("asdfkjasldkfjalsdfja%@$#^&*(^%$#")