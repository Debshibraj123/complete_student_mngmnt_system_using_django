from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages

def HOME(request):
    return render(request, 'Staff/home.html')

def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)

    for i in staff:
        staff_id = i.id

        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
          'notification' : notification  
        }

        return render(request, 'Staff/notificatiion.html', context)
    
def MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('notification')

def STAFF_APPLY_LEAVE(request):
    return render(request, 'Staff/apply_leave.html')

def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_leave(
            staff_id=staff,
            leave_date=leave_date,
            message=leave_message,
        )

        leave.save()
        messages.success(request, "Successfully Applied For Leave")

        return redirect('staff_apply_leave')


def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
         'staff_leave_history':staff_leave_history,
        }
        return render(request, 'Staff/apply_leave.html', context)
    
def STAFF_FEEDBACK(request):
    
    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

    context = {
     'feedback_history':feedback_history,
    }

    return render(request, 'Staff/feedback.html', context)

def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
          staff_id = staff,
          feedback = feedback,
          feedback_reply = "",    
        )

        feedback.save()
        messages.success(request,"Your Feedback has been Submitted Successfully!")
        return redirect("staff_feedback")
    

def STAFF_TAKE_ATTENDENCE(request):
    if request.user.is_authenticated:
        staff, created = Staff.objects.get_or_create(admin=request.user)

        subject = Subject.objects.filter(staff=staff)
        session_year = Session_Year.objects.all()

        action = request.GET.get('action')
        
        # get_subject = None
        # get_session_year = None

        if action is not None:
            if request.method == 'POST':
                subject = request.POST.get('subject_id')
                session_year_id = request.POST.get('session_year_id')

                # get_subject = Subject.objects.get(id = subject)
                # get_session_year = Session_Year.objects.get(id = session_year_id)
                

        context = {
            'subject': subject,
            'session_year': session_year,
            # 'get_subject': get_subject,
            # 'get_session_year':get_session_year
        }

        return render(request, 'Staff/take_attendence.html', context)
    else:
        # Handle the case where the user is not authenticated
        return render(request, 'error_page.html', {'error_message': 'User is not authenticated'})