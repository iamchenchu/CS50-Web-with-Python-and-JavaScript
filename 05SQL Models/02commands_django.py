"""
install django  : pip install django
check the version : django-admin --version
CREATE PROJECT : django-admin startproject airline 
go to the project : cd airline
create the first app : python manage.py startapp flights
now add the app into the main project : Go to airline -> settings.py -> installed_apps -> add flights app there 
now go to urls.py and add the paths there in the urlpatterns : path("flights/", include("flights.urls")) [also import include from django.urls]
now create urls.py inside our new app which is flights : from django.urls import path,include;     from . import views    
urlpatterns = [
    path("flights/",include("flights.urls")) # If some one types flights/ something then it should take them to flights.urls
]
Now I need a urls.py in flights so let's go and create urls.py in flights 
code : from django.urls import path
from . import views
url 

python manage.py makemigrations : to start migrations 
python manage.py migrate : apply the migrations 

run the server : py manage.py runserver
create an app : py manage.py startapp members
"""