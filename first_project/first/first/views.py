from curses.ascii import HT
from django.http import HttpResponse

def homepage(request) :
    return HttpResponse("This is Home page")

def blog(request, id) :
    return HttpResponse(f"blog {id}")