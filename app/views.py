from django.shortcuts import render


def indexView(request):
    return render(request, "index.html")
def aboutView(request):
    return render(request, "about.html")


