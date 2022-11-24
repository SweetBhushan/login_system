from django.shortcuts import HttpResponse, render, HttpResponseRedirect,redirect
from django.contrib import messages
from .models import studentRegistration
from .forms import studentform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
    if request.method =="POST":
     fm= studentform(request.POST)
     if fm .is_valid():
      fm.save()
     messages.success(request,'sign_up succesfull   !!')
    else:
       fm= studentform()
    return render(request, 'enroll/sign_up.html',{'form':fm})    
               
def login_up(request):
    if request.method =="POST":
        fm= AuthenticationForm(request=request,data=request.POST)
        if fm .is_valid():
            uname= fm.cleaned_data['username']
            upass= fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            
            if user is not None:
                login(request,user)
        return HttpResponseRedirect('/profile/')
    else:
        fm= AuthenticationForm()
    return render (request, 'enroll/login.html',{'form':fm})

def  usre_profile(request):
    return render(request, 'enroll/profile.html')



