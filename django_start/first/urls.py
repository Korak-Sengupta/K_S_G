from django.contrib import admin
from django.urls import path,include
from first import views

admin.site.site_header = "Korak's Loda"
admin.site.site_title = "KSG"
admin.site.index_title = "Welcome to A Portal Where korak will show his loda"




urlpatterns = [
    path("", views.index,name='first'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("home", views.home,name='home'),
]
