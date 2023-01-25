from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core.mail import send_mail
from .forms import *
from .models import Doner_details

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

# Registration of donar
def donar_register(request):
    if request.method == 'POST':
        f = register(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['dd_username']
            fmail = f.cleaned_data['dd_email']
            f.save()
            messages.success(request,'Registered successfully...')
            subject = 'Food Waste Management System'
            message = f'Hi {fname} thanks for registering ...'
            sender = settings.EMAIL_HOST_USER
            send_mail(subject,message,sender,[fmail])
    else:
        f = register()
    return render(request,'donar_register.html',{'data':f})


def donarlogin(request):
    if request.method == 'POST':
        f = donarloginform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['username']
            fpwd = f.cleaned_data['password']
            user = authenticate(request,username=fname,password = fpwd)
            if user is not None:
                return render(request,'donarhome.html')
    else:
        f = donarloginform()
        return render(request,'donarlogin.html',{'data':f})