from django.shortcuts import render
from .forms import ImageForm
from .models import SampleImage
from PIL import Image
import cv2
import numpy as np
import os
import joblib
import shutil

# Create your views here.
def home(request):
    status = ""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            status = "File uploaded successful"
   
    form = ImageForm()
    img = SampleImage.objects.all()
    x = len(img) - 1;
    img = img[x]
   
    return render(request, 'home.html', {'status':status, 'img':img, 'form':form})

def output(request):
    
    img = SampleImage.objects.all()
    x = len(img) - 1;
    img = img[x]
    path = img.sample.url

    path = path[1:len(path)]
    xray_image = cv2.imread(path)
    knn_model = joblib.load('model.sav')
    image_size = 32
    test_sample = cv2.resize(xray_image, (image_size, image_size),interpolation = cv2.INTER_AREA).reshape(1,-1)
    result = knn_model.predict(test_sample)
    print(result)
    shutil.rmtree('media')

    return render(request, 'output.html',{'result':result})