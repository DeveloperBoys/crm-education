from django.shortcuts import render
from django.http import HttpResponse


def student_home(request):
    return HttpResponse("<h1>Student Home</h1>")
