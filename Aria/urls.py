from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('terms-conditions',views.terms,name="terms")
    
]