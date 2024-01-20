from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages


# @login_required
def HOME(request):
    return render(request,'HOD/home.html')

def ADD_STUDENT(request):

    course = Course.objects.all()
    season_year = Session_Year.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        course = request.POST.get('course')
        session_year = request.POST.get('session_year')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "email already exist")
            return redirect('add_student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "username already exist")
            return redirect('add_student')
        
        else:
            user = CustomUser(
               first_name = first_name,
               last_name = last_name,
               username = username,
               email = email,
               user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course)
            session_year = Session_Year.objects.get(id = session_year)
            

            student = Student(
              admin = user,
              address = address,
              gender = gender,
              session_year = session_year,
              course = course,
            )

            student.save()
            messages.success(request, user.first_name + " " + user.last_name , "Your Profile Has been Successfully added")
            return redirect('add_student')
            

    context = {
      'course':course,
      'seassion_year':season_year    
    }
    return render(request, 'Hod/add_student.html', context)


def VIEW_STUDENT(request):

    student = Student.objects.all()
    

    context = {
      'student':student
    }
    return render(request, 'Hod/view_student.html',context)

def EDIT_STUDENT(request, id):
    
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    seassion_year = Session_Year.objects.all()

    context = {
       'student':student,
       'course': course,
       'seassion_year':seassion_year,
    }
    
    return render(request, 'Hod/edit_student.html', context)

def UPDATE_STUDENT(request):
    
    if request.method == "POST":
        
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        course = request.POST.get('course')
        session_year = request.POST.get('session_year')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        # Check if the new username is unique
        if CustomUser.objects.filter(username=username).exclude(id=student_id).exists():
            messages.error(request, "Username is already taken. Please choose a different one.")
            return render(request, 'Hod/edit_student.html')

        user.username = username

        if password != None and password != '':
            user.set_password(password)
        
        try:
            user.save()
        except IntegrityError:
            messages.error(request, "Username is already taken. Please choose a different one.")
            return render(request, 'Hod/edit_student.html')

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id=course)
        student.course = course

        session_year = Session_Year.objects.get(id=session_year)
        student.session_year = session_year

        student.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('view_student')
        
    return render(request, 'Hod/edit_student.html')


def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request, 'Record are Successfully deleted')
    return redirect('view_student')