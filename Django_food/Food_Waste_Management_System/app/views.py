from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .forms import *
from .models import *

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
        f = Donar_form(request.POST)
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
        f = Donar_form()
    return render(request,'donar_register.html',{'data':f})
