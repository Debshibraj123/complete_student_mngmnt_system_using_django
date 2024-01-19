from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )


    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
    username = models.CharField(max_length=30, unique=True, default='default_username')

    def save(self, *args, **kwargs):
        # Ensure that existing rows with a null value for 'username' get a default value
        if not self.username:
            self.username = 'default_username'
        super().save(*args, **kwargs)

class Course(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start

#add student model
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='students_in_course')
    session_year = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING, related_name='students_in_session_year')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name