from django.shortcuts import render, redirect

def STUDENT_HOME(request):
    return render(request, 'Student/home.html')