from django.shortcuts import render


tasks =["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/CS 50 Web with Python and JavaScript/04Django/project_one/tasks/templates/tasks/index.html", {
        "tasks":tasks
    })

def add(request):
    return render(request, "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/CS 50 Web with Python and JavaScript/04Django/project_one/tasks/templates/tasks/add.html")

