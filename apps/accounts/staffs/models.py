from django.db import models
from apps.accounts.models import CustomUser


class Staffs(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    coming_days = models.DateTimeField()
    working_percentage = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)