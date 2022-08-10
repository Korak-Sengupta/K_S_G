from turtle import home
from django.contrib import admin
from django.urls import path,include
from first import views

admin.site.site_header = "Korak's Den"
admin.site.site_title = "KSG"
admin.site.index_title = "Welcome to KSG's Portal"




urlpatterns = [
    path("", views.index,name='first'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("home", views.home,name='home'),
]
