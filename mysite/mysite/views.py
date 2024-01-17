from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
#import messages
from django.contrib import messages


def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

        if user!=None:
            login(request, user)
            user_type= user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type=='2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                #message
                messages.error(request, 'Email and Password')
                return redirect('login')
        else:
            return  redirect('login')
    return None

def doLogout(request):
    logout(request)
    return redirect('login')