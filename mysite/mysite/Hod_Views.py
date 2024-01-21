from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.http import Http404



@login_required(login_url='/')
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

def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
          name = course_name
        )
        course.save()
        messages.success(request, 'Course Added Successfully!')
        return redirect('add_course')


    return render(request, 'Hod/add_course.html')
  


def VIEW_COURSE(request):
    
    course = Course.objects.all()

    context = {
       'course':course   
    }
    
    return render(request, 'Hod/view_course.html', context)

def EDIT_COURSE(request, id):
    course = Course.objects.get(id = id)

    context = {
      'course': course
    }
    return render(request, 'Hod/edit_course.html', context)


def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course_id = request.POST.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise Http404("Course not found")

        course.course_name = name
        course.save()
        messages.success(request, "Course Updated")
        return redirect('view_course')

    return render(request, 'Hod/edit_course.html')


def DELETE_COURSE(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, "Successfully Deleted")

    return redirect('view_course')

def ADD_STAFF(request):

    if request.method == "POST":
        #student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email = email).exists():
            messages.error(request,"Email already exists.")
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.error(request,"Username already exists.")
            return redirect('add_staff')
        

        else:
            user = CustomUser(first_name=first_name, last_name=last_name, email=email, username=username,user_type = 2)
            user.set_password(password)
            user.save()

            staff = Staff(
              admin = user,
              address = address,
              gender = gender
            )
            staff.save()
            messages.success(request,"Staff added Successfully!")
            return redirect("add_staff")
        return redirect(request, 'Hod/add_staff.html')



    return render(request, 'Hod/add_staff.html')

def VIEW_STAFF(request):
    staff=Staff.objects.all()
    context={'staff':staff}
    return render(request, 'Hod/view_staff.html', context)

def EDIT_STAFF(request, id):
    staff = get_object_or_404(Staff, id=id)
    context = {'staff': staff}
    return render(request, 'Hod/edit_staff.html', context)

def UPDATE_STAFF(request):

    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address =  request.POST.get('address')
        gender =  request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != '':
            user.set_password(password)

        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,'Profile Updated Successfully!')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')

def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,"Deleted Successfully")

    return redirect('view_staff')

def ADD_SUBJECT(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        courses = request.POST.get('course')
        staffs = request.POST.get('staff')

        course = Course.objects.get(id = courses)
        staff = Staff.objects.get(id = staffs)

        subject = Subject(
          name = subject_name,
          course = course,
          staff = staff
        )

        subject.save()
        messages.success(request,"Subject Added Successfully")
        return redirect('add_subject')
    

    context = {
        'course':course,
        'staff':staff,
    }



    return render(request, 'Hod/add_subject.html', context)

def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context={
        'subject' : subject
        }
    return render(request, 'Hod/view_subject.html', context)