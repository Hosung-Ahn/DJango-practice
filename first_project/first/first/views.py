from curses.ascii import HT
from django.http import HttpResponse

def homepage(request) :
    return HttpResponse("This is Home page")

def blog(request, id) :
    return HttpResponse(f"blog {id}")

def add(request, n1, n2) :
    n1 = float(n1)
    n2 = float(n2)
    return HttpResponse(n1+n2)