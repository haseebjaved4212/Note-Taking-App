from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    return render(request)("Hello, world. You're at the app index.")
# Create your views here.
