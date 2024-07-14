import random
from django.shortcuts import render, redirect, HttpResponse
import requests
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser
from django import forms

def BASE(request):
    return render(request, "base.html")
def LOGIN(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method =="POST":  
        user = EmailBackend.authenticate(request,username=request.POST.get('email'), password=request.POST.get('password'))
        if user!=None:
            login(request, user)
            user_type=user.user_type
            if user_type=='1':
                return redirect("hod_home")
        
            elif user_type=='2':
                return redirect("staff_home")
                
            else:
                messages.error(request,"Email and Password are Invalid")
                return redirect('login')
        else:
            messages.error(request,"Email and Password are Invalid")
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')  


@login_required(login_url="/")
def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url="/")
def PROFILE_UPDATE(request):
    if request.method=="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id=request.user.id)   
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic=profile_pic

            if password!=None and password!="":
                customuser.set_password(password)
            if profile_pic!=None and profile_pic!="":
                customuser.profile_pic=profile_pic
            customuser.save()
            messages.success(request, "Your Profile Updated Successfully !")
            return redirect('profile')

        except:
            messages.error(request, "Profile Updation Failed")

    return render(request, 'profile.html')

def FETCH_BOOK_DATA(request):
    if request.method == "POST":
        query = request.FILES.get("query")
        url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{query}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get('items', [])
            print(results)

    return render(request, '../templates/base.html', {'results': results})