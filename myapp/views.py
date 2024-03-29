from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def website(request):
    return HttpResponse("<h1>This is the Website page</h1>")

def home(request):
    return HttpResponse('<h2>This is the Home page</h2>')

def contact(request):
    return HttpResponse("<h3>This is the Contact page</h3>")


def about(requset):
    return HttpResponse("<h4>This is the About page</h4>")