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


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
