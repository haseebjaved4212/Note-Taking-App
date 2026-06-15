from .views import renderSomething, aboutSomething
from django.urls import path

urlpatterns = [
    path("", renderSomething, name="render"),
    path("about", aboutSomething, name="about"),
]