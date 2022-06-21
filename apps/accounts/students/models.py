from django.db import models
from apps.accounts.models import CustomUser

class Students(models.Model):
    GENDER_CHOICES = (
        ('YIGIT', 'Yigit'),
        ('QIZ', 'Qiz') 
    )
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    profile_pic = models.FileField()
    phone_number = models.CharField(max_length=9)
    coming_day = models.DateTimeField()
    first_lesson_day = models.DateTimeField()
    in_queue = models.BooleanField(default=True)
    address = models.TextField()
    group = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)