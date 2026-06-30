from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Eloksignature!</h1>")

def about(request):
    return HttpResponse("<h1>About</h1><p>This is a simple To-Do application built with Django.</p>")

def contact(request):
    return HttpResponse("<h1>Contact Us</h1><p>Email: etzelvisbrightfuture@gmail.com</p>")
