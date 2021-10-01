from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('loginuser',views.loginuser, name="loginuser"),
    path('userdetail',views.userdetail, name="userdetail"),
    path('updateuser',views.updateuser, name="updateuser"),
    path('deleteuser',views.deleteuser, name="deleteuser"),
    path('logoutuser',views.logoutuser, name="logoutuser")
]
