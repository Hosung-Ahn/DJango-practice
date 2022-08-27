from curses.ascii import HT
from django.http import Http404, HttpResponse, HttpResponseNotFound

fruits = {
    'red' : 'apple',
    'yellow' : 'banana',
    'green' : 'water melon'
}

infos = {
    'name' : 'hosung',
    'age' : 25,
    'email' : 'an3735297@naver.com'
}

def homepage(request) :
    return HttpResponse("This is Home page")

def blog(request, id) :
    return HttpResponse(f"blog {id}")

def add(request, n1, n2) :
    n1 = float(n1)
    n2 = float(n2)
    return HttpResponse(n1+n2)

def fruit(request, color) :
    try :
        result = fruits[color]
        return HttpResponse(result)
    except :
        result = "No page for that color!"
        return HttpResponseNotFound(result)
    
def privacy(request, info) :
    try : 
        result = infos[info]
        return HttpResponse(result)
    except :
        raise Http404("There is no infomation.")