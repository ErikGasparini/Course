from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def erik(request):
    return HttpResponse("Hello, Erik!")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
#   return HttpResponse(f"Hello, {name.capitalize()}!")
