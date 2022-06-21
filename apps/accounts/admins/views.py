from django.shortcuts import render
from apps.accounts.students.models import Students
from apps.accounts.staffs.models import Staffs
from django.http import HttpResponse

def admin_home(request):
    all_student_count = Students.objects.all().count()
    subject_count = 0 # Subjects.objects.all().count()
    course_count = 0 # Courses.objects.all().count()
    staff_count = 0 # Staffs.objects.all().count()

    context={
        "all_student_count": all_student_count,
        "subject_count": subject_count,
        "course_count": course_count,
        "staff_count": staff_count,
    }
    return render(request, "hod_template/admin_profile.html", context)
    # return HttpResponse("<h1>Admin Home</h1>")
    
