from typing import Protocol
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from accounts.models import Consumer
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=="POST":
        username = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['pass']
        repassword = request.POST['re_pass']
        if password != repassword:
            return redirect('index')
        else:
            obj = User.objects.create_user(username,email,password)
            obj.first_name = username
            obj.is_active = True
            obj.save()
            cobj = Consumer(user=obj,email=email,address=address,password=password)
            cobj.save()
            return redirect('login')

def loginuser(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['pass']

        if User.objects.filter(email = email).exists:
            userdetails = User.objects.get(email = email)
            userlog = authenticate(username = userdetails.username, password = password)
            login(request,userlog)
            print(userdetails)
            return redirect('userdetail')

def userdetail(request):
    print(request.user)
    u = Consumer.objects.get(user_id= request.user.id)
    param = {"username": u.user, "email" : u.email, "address" : u.address}
    return render(request,'editprofile.html',param)

def updateuser(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        u = Consumer.objects.get(user_id=request.user.id)
        us = User.objects.get(id=request.user.id)
        us.username = username
        us.save()
        u.email = email
        u.address = address
        u.save()
        return redirect('userdetail')
    
def deleteuser(request):
    if request.user.is_authenticated:
        us = User.objects.get(id=request.user.id)
        us.delete()
        return redirect('login')

def logoutuser(request):
    logout(request)
    messages.success(request,"Logout Successfull")
    return redirect('login')

        

        
 



