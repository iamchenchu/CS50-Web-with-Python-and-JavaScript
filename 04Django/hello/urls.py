from django.urls import path
from . import views # . means current direcory, importing views from the cd

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("chenchu", views.chenchu, name="chenchu"),
    path("rajia", views.rajia, name="rajia")
]
