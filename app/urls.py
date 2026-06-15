from .views import indexView, aboutSomething
from django.urls import path

urlpatterns = [
    path("", indexView, name="index"),
    path("about", aboutSomething, name="about"),
]