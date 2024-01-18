from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# @login_required
def HOME(request):
    return render(request,'HOD/home.html')

def ADD_STUDENT(request):
    return render(request, 'Hod/add_student.html')