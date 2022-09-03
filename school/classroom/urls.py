from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank/', views.ThankYouView.as_view(), name='thank'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create/', views.TeacherCreateView.as_view(), name='create'),
    path('list/', views.TeacherListView.as_view(), name='list'),
    path('detail/<int:pk>', views.TeacherDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.TeacherDeleteView.as_view(), name='delete'),
]
