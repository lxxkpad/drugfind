from django.shortcuts import render

from .forms import UploadForm
#from django.utils.timezone import datetime
import os
import random
import numpy as np
import cv as cv2

def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #เปิดไฟล์ในโฟลเดอร์ media ตามที่ได้สร้างเอาไว้ โดยใช้ชือเดียวกับไฟล์ที่อัปโหลดขึ้น
            #เพื่อเขียน (w) ในโหมดไบนารี (b) ถ้ายังไม่มีอยู่ก่อน ให้สร้างขึ้นใหม่ (+)
            with open(f'media/upload/{file.name}', 'wb+') as target:
                #แบ่งไฟล์เป็นส่วนย่อยๆ แล้วนำมาเขียนลงในไฟล์เป้าหมายต่อเนื่องกันจนครบ
                for chunk in file.chunks():
                    target.write(chunk)
                #หรืออ่านเนื้อหาของไฟล์ทั้งหมด แล้วเขียนพร้อมกันทีเดียว
                #โดยไม่ต้องใช้ลูป for แต่ไม่ควรกับไฟล์ที่มีขนาดใหญ่
                #target.write(f.read())
        else:
            file = None
    else:
        form = UploadForm()
        file = None
    return render(request, 'index.html', {'form':form, 'file':file})

def about(request):
    #return HttpResponse('About us')
    return render(request, 'aboutus.html')

def druglists(request):
        #return HttpResponse('Drug lists')
    return render(request, 'druglists.html')

def contact(request):
    #return HttpResponse('Team contact')
    return render(request, 'contact.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        def save_file(dir, file):
            if not dir.endswith('/'):
                dir += '/'

            with open(f'{dir}{file.name}', 'wb+') as target:
                for chunk in file.chunks():
                    target.write(chunk)
        def get_unique_name(dir, filename):
            if not dir.endswith('/'):
                dir += '/'
            
            if os.path.exists(f'{dir}{filename}'):
                sp = filename.split('.', 1)
                name = sp[0]
                ext = sp[1]
                r = random.randint(1000, 10000)
                return f'{name}.{ext}'
            else:
                return filename
        if form.is_valid():
            file = request.FILES['file']
            file.name = get_unique_name('media/upload/', file.name)
            save_file('media/upload/', file)

        else:
            file = None

    else:
        form = UploadForm()
        file = None
    
    return render(request, 'predictdrugclass.html', {'form':form, 'file':file})
