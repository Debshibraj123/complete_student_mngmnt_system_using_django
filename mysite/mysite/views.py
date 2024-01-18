from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from app.models import CustomUser


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

def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    
    context = {
       "user": user,    
    }
    return render(request, 'profile.html')


def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pics')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic

            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully')
            redirect('profile')


        except:
            messages.error(request, 'Your Profile has not Updated')
    return render(request, 'profile.html')

