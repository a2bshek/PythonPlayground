from django.urls import path
from blogger import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('signup', views.signup, name='signup'),
    path('comments', views.comments, name='comments'),
]