from django.shortcuts import render
from django.http import Http404, HttpResponse


# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")


texts = ["Lorem ipsum... ",
         "Praesent",
         "Morbi"]


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404("No such section")
