
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

#login credentials
# admin username='admin'
# admin password='admin'

def post(request):
    return render(request,"post.html")

def login(request):
    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(request,username=name, password=password)
        if user is not None:
            # login(request, user)
            print("you are logged in !")
            messages.success(request, "You have been logged in successfully !")
            return render(request,"post.html")
           
        else:
            print("Return an 'invalid login' error message.")
            messages.error(request, 'Sorry! Please check your email Id and password.')
            return render(request,'login.html')

    return render(request,'login.html')