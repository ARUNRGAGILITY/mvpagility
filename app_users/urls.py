from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/', views.profile, name="profile"),

    path('', views.home, name="home"),
    path('user-home/', views.user_home, name="user-home"),
    path('django-learning/', views.django_learning, name="django-learning"),
    #path('my-todolist/', include('todolist.urls'), name='my-todolist'),
   
]
