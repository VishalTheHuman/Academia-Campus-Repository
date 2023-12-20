from django.db import models

class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    ]

    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)
    roll_number = models.CharField(max_length=20, blank=True, null=True)
    teacher_id = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)  
    forgot = models.CharField(max_length=100,default='None')

    def __str__(self):
        return self.email