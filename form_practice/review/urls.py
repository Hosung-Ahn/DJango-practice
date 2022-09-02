from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('start/', views.start, name='start'),
    path('end/', views.end, name='end'),
]
