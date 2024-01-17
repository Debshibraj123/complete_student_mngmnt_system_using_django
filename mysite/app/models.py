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