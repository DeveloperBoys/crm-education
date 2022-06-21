from django.shortcuts import render
from django.http import HttpResponse


def staff_home(request):
    return HttpResponse("<h1>Staf Home</h1>")
