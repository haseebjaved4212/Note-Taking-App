from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    return render(request, "index.html")
def aboutView(request):
    return render(request, "about.html")

# Create your views here.
