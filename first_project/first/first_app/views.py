from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse("This is View in app")

def simple_view(request) :
    return render(request, 'first_app/example.html')