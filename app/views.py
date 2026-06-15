from django.shortcuts import render
from django.http import HttpResponse

def renderSomething(request):
    return render(request, "index.html")

def aboutSomething(request):
    return HttpResponse("My About Page")


# Create your views here.
