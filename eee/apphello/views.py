from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from apphello.models import registermodel
from apphello.forms import women

# def son(request):
#     if request.method=='POST':
#         s1=request.POST['god']
#         s2=request.POST['angle']
#         phone=request.POST['phone']
#         gender=request.POST['gender']
#         # print(s1,s2)
#         man.objects.create(god=s1,angle=s2,phone=phone,gender=gender)
#         return HttpResponse('values are insert')
#     if request.method=='GET':
#         form=women()    
#     context={'form':form}
#     return render(request,'see.html',context)
