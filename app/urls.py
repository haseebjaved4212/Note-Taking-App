from .views import indexView, aboutView 
from django.urls import path

urlpatterns = [
    path("", indexView, name="index"),
    path("about", aboutView, name="about"),
]