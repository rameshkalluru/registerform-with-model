import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from ramya.models import ram
from ramya.forms import rammy

def lovely(request):
    if request.method=='POST':
        rollno=request.POST['rollno']
        name=request.POST['name']
        age=request.POST['age']
        password=request.POST['password']
        repassword=request.POST['repassword']
        email=request.POST['email']
        url=request.POST['url']
        image=request.POST['image']
        file=request.POST['file']
        gender=request.POST['gender']
        dob=request.POST['dob']
        if password==repassword:
           print(ram.objects.create(rollno=rollno,name=name,age=age,password=password,
        repassword=repassword,email=email,url=url,image=image,file=file,gender=gender,dob=dob))
        else:
            return HttpResponse('passwords are not match')
        return HttpResponse('values are insert')
    if request.method=='GET':
        form=rammy()
    context={'form':form}
    return render(request,'saw.html',context)