from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank/', views.ThankYouView.as_view(), name='thank'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('crate/', views.TeacherCreateView.as_view(), name='create'),
    path('list/', views.TeacherListView.as_view(), name='list'),
]
