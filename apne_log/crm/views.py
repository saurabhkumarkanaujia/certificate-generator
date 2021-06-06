from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Certificate

# Create your views here.

def user_details(request):
    data=Certificate.objects.all()
    return render(request,'user_details.html',{'c_data':data})

def add_new(request):
    if request.method == 'POST':
        name1=request.POST['name']
        college1=request.POST['college']
        dept1=request.POST['dept']
        start1=request.POST['start']
        end1=request.POST['end']
        certificate_data = Certificate(name=name1, college=college1, dept_name=dept1, start=start1, end=end1)
        certificate_data.save();
        messages.success(request,'Details Inserted')
        return redirect('user_details')
    else:
        return render(request,'add_new.html')