from django.urls import path
from . import views


# project urls 에서 app url을 추가할 때 'first_app/' 을 추가해줬으므로
# 아래 urlpatterns에서는 path 를 ''으로 비워도 자동으로 'first_app/'이 추가된다.
# 'second' 라고 한다면 'first_app/second' 가 추가된다.
urlpatterns = [
    path('', views.index, name='index')
]
