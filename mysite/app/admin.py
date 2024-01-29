from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ('username', 'user_type')
    
admin.site.register(CustomUser, UserModel) 
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_leave)
admin.site.register(Staff_Feedback)
admin.site.register(Attendence)
admin.site.register(Attendence_Report)