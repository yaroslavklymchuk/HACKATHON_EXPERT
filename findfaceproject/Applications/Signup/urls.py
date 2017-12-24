from django.conf.urls import url, include
from django.contrib import admin
from findfaceproject.Applications.Signup import views



urlpatterns = [
    url(r'^', views.get_name),
]