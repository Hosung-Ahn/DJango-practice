from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from . import forms

# Create your views here.

# function based view
# def home_view(request) :
#     return render(request, 'classroom/home.html')


# class based view
class HomeView(TemplateView) :
    template_name = 'classroom/home.html'
    
class ThankYouView(TemplateView) : 
    template_name = 'classroom/thankyou.html'
    
class ContactFormView(FormView) :
    form_class = forms.ContactForm
    template_name = 'classroom/contact.html'
    
    # url 주소임을 유의 (html 아님)
    success_url = reverse_lazy('classroom:thank')
    
    def form_valid(self, form) :
        print(form.cleaned_data)
        return super().form_valid(form)
        