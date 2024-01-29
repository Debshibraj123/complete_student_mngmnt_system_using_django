from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages
from django.http import Http404



# @login_required(login_url='/' )
def HOME(request):

    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()

    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female' : student_gender_female
        }

    return render(request,'HOD/home.html', context)

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
            user.set_password = password
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

def EDIT_SUBJECT(request, id):
    
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
       'subject':subject,
       'course':course,
       'staff':staff
    }

    return render(request, 'Hod/edit_subject.html', context)


def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course')
        staff_id = request.POST.get('staff')

        # Use get_object_or_404 to retrieve Course and Staff instances
        course = get_object_or_404(Course, id=course_id)
        staff = get_object_or_404(Staff, id=staff_id)

        subject = Subject(
            id=subject_id,
            name=subject_name,
            course=course,
            staff=staff,
        )

        try:
            subject.save()
            messages.success(request, 'Successfully edited the information')
            return redirect('view_subject')
        except Exception as e:
            # Handle the exception, you can print it for debugging purposes
            print(e)
            messages.error(request, 'An error occurred while updating the subject.')
            
    # If the method is not POST or if there was an error, render the form again
    subject = Subject.objects.get(id=subject_id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject': subject,
        'course': course,
        'staff': staff
    }

    return render(request, 'Hod/edit_subject.html', context)



def DELETE_SUBJECT(request, id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request, 'Subject deleted Successfully')
    return redirect('view_subject')


def ADD_SESSION(request):
    if request.method == 'POST':
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        session = Session_Year(
           session_start = session_year_start,
           session_end = session_year_end
        )
        session.save()
        messages.success(request,'Session added successfully!')
        return redirect('add_session')

    return render(request, 'Hod/add_session.html')




def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context = {
      'session':session    
    }

    return render(request, 'Hod/view_session.html', context)

# def EDIT_SESSION(request, id):
#     session = Session_Year.objects.filter(id = id)
    
#     context = {
#        'session':session, 
#     }
#     return render(request, 'Hod/edit_session.html', context)

def DELETE_SESSION(request, id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.error(request,"The data has been deleted")
    return redirect('view_session')

def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
      'staff':staff,
      'see_notification':see_notification,
    }
    
    return render(request, 'Hod/staff_notification.html', context)


def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message =  request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)

        notification = Staff_Notification(
          staff_id = staff,
          message = message,    
        )
        notification.save()
        messages.success(request, "Message Sent Successfully")
        return redirect('staff_send_notification')
    

def STAFF_LEAVE_VIEW(request):

    staff_leave = Staff_leave.objects.all()

    context = {
      'staff_leave':staff_leave,
    }

    return render(request, 'Hod/staff_leave.html', context)

def STAFF_APPROVE_LEAVE(request, id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

def STAFF_DISAPPROVE_LEAVE(request, id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')

def STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()

    context = {
       'feedback':feedback,    
    }


    return render(request, 'Hod/staff_feedback.html', context)


def STAFF_FEEDBACK_SAVES(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()

        messages.success(request, 'Successfully Done')
        return redirect('staff_feedback')
    
def STUDENT_SEND_NOTIFICATION(request):

    student = Student.objects.all()

    context = {
      'student': student    
    }
     

    return render(request, 'Hod/student_notification.html')