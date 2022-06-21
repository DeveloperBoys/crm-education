from django.urls import path, include
from apps.accounts.admins.views import admin_home
from apps.accounts.staffs.views import staff_home
from apps.accounts.students.views import student_home


urlpatterns = [
    path('admin_home/', admin_home, name='admin_home'),
    path('staff_home/', staff_home, name='staff_home'),
    path('student_home/', student_home, name='student_home'),
]