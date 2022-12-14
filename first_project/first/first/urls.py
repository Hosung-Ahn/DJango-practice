"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('first_app/', include('first_app.urls')),
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('blog<int:id>', views.blog),
    path('add/<str:n1>/<str:n2>', views.add),
    path('fruit/<int:num>', views.num_fruit),
    path('fruit/<str:color>', views.fruit, name='fruit-view'),
    path('privacy/<str:info>', views.privacy),
]
