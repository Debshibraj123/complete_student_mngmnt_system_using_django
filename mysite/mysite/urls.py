from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .Hod_Views import HOME

from .import views,Hod_Views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('Hod/Home', Hod_Views.HOME, name='hod_home'),

    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_Views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin>', Hod_Views.DELETE_STUDENT, name='delete_student'),
    path('Hod/Course/Add', Hod_Views.ADD_COURSE, name='add_course'),
    path('Hod/Course/View', Hod_Views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>', Hod_Views.EDIT_COURSE, name='edit_course'),
    path('Hod/Course/Update', Hod_Views.UPDATE_COURSE, name='update_course'),
   
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
