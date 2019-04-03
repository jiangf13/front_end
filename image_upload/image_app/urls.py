from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('image_upload', people_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'), 
    path('people_images', display_people_images, name = 'people_images'),
] 
  
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 