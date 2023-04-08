from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.web_home, name="web_home"),

]