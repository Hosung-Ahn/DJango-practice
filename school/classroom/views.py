from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from . import forms
from . import models

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
        
class TeacherCreateView(CreateView) :
    # submit 시 model을 자동으로 저장해준다.
    model = models.Teacher
    # CreateView 는 model_form.html 인 템플릿을 자동으로 찾는다.
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank')
    
class TeacherListView(ListView) :
    model = models.Teacher
    # model_list.html 인 템플릿을 자동으로 찾는다.
    
    # model에 있는 데이터 다루기
    queryset = models.Teacher.objects.order_by('first_name')
    
    context_object_name = 'teacher_list'
    
class TeacherDetailView(DetailView) :
    # 하나의 model entry 를 반환한다.
    model = models.Teacher 