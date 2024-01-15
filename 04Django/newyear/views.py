from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/CS 50 Web with Python and JavaScript/CS50-Web-with-Python-and-JavaScript/04Django/PROJECT_One/newyear/templates/newyear/index.html", {
        "newyear": now.month == 1 and now.day ==1
    })
