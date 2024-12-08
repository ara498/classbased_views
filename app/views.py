from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *


#FBV for returning string as Response
def fbv_string(request):
    return HttpResponse('<h1>This is fbv_string</h1>')


#CBV for returning string as Response
class cbvstring(View):
    def get(self,request):
         return HttpResponse('<h1>This is cbvstring</h1>')  



#FBV for returning string as HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')    

#FBV for returning string as HTML page

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')      

#insert_student_fbv

def insert_student_fbv(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Successfully Done')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_student_fbv.html',d)


#insert data by using student in classbasedview

class Cbv_CreateStudent(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'Cbv_CreateStudent.html',d)
    
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done successfully')
        else:
            return HttpResponse('Invalid data')