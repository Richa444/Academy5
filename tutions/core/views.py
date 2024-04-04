from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from . import views

def contact(request):
    if request.method == 'POST': 
      fm = ContactForm(request.POST)
      if fm.is_valid():
        nm = fm.cleaned_data['name']
        email = fm.cleaned_data['email']
        phone_number = fm.cleaned_data['phone_number']
        message = fm.cleaned_data['message']
        fm = ContactMessage(name=nm,email=email,phone_number=phone_number,message=message)
        print(nm)
        print(email)
        print(phone_number)
        print(message)
       
        fm.save()
        fm = ContactForm()
    else: 
      fm = ContactForm()
      
    return render(request, 'core/contact.html',{'form':fm})

def programdetail(request):
    return render(request, 'core/programdetail.html')
def home(request):
    return render(request, 'core/home.html',{'title':'this is home'})

def index(request):
    return render(request, 'core/index.html',{'title':'this is home'})

def about(request):
    return render(request, 'core/about.html',{'title':'this is home'})

def program(request):
    return render(request, 'core/program.html',{'title':'this is home'})

def base1(request):
    return render(request, 'core/base1.html',{'title':'this is base1'})