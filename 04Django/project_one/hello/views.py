from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/CS 50 Web with Python and JavaScript/04Django/project_one/hello/templates/hello/index.html")

def chenchu(request):
    return HttpResponse("Hello chenchu How are you ?")

def rajia(request):
    return HttpResponse("hey rajia how are you ?")

def greet(request, name):
    return render(request, "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/CS 50 Web with Python and JavaScript/04Django/project_one/hello/templates/hello/greet.htm", {
        "name": name.capitalize()
    })