from django.urls import path
from . import views


# app namespace 를 등록한다.
app_name = "my_app"

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable', views.variable_view, name='variable'),
    path('template_inheritence', views.template_inheritence_view),
]
