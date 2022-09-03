from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# function based view
# def home_view(request) :
#     return render(request, 'classroom/home.html')


# class based view
class HomeView(TemplateView) :
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView) : 
    template_name = 'classroom/thankyou.html'