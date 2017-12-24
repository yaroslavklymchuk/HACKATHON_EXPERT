from django.conf.urls import url, include
from django.contrib import admin
from findfaceproject.Applications.Home import views

urlpatterns = [
    url(r'^', views.ResponseForHome),

]
