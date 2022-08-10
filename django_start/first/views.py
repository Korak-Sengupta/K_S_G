from django.shortcuts import render, HttpResponse
from first.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context={
    }
    return render(request,'index.html',context)
    #return  HttpResponse("this is homepage") #string is sent 
def about(request):
    return render(request,'about.html') #sends to respective pages
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')       #get info from the form
        desc=request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc)    #store in a object
        contact.save()
        messages.success(request, 'Your message is sent')
     
    return render(request,'contact.html')
def home(request):
    return render(request,'index.html')

