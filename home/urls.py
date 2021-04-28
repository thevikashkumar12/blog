from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='name'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("LCD", views.LCD, name='LCD'),
    path("fridge", views.fridge, name='fridge'),
    path("washing", views.washing, name='washing'),
    path("mobile", views.mobile, name='mobile'),
    path("contact", views.contact, name='contact'),
]
