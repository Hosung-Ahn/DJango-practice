from django.shortcuts import render

# Create your views here.
def example_view(request) :
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request) :
    
    var = {"first_name" : "Ahn", "second_name" : "Hosung",
           "lst" : [1,2,3,4],
           "fruit" : {"apple" : "red", "banana" : "yellow"}}
    # view 에서 template 로 매개변수를 전달할 수 있다.
    return render(request, 'my_app/variable.html', context=var)

def template_inheritence_view(request) :
    return render(request, 'my_app/template_inheritence.html')