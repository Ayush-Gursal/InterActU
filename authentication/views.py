
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import  CreateUserForm 
from .models import *




@login_required(login_url='login')
def home(request):
     context={}
     return render(request,'authentication/home.html',context)


def rental(request):
     context={}
     return render(request,'rental/hostel.html',context)

def store(request):
     context={}
     return render(request,'store/store.html',context)
def notice(request):
     context={}
     return render(request,'notice/noticeboard.html',context)

def loginPage(request):
     

    if request.user.is_authenticated:
          return redirect('home')
    else:
          
          if request.method=='POST':
               username=request.POST.get('username')
               password=request.POST.get('password')
      
               user =authenticate(request,username=username,password=password)
      
               if user is not None:   
                    login(request,user)
                    return redirect('home')
               else:
                    messages.info(request,'Username or password is incorrect')
          context={}
          return render(request,'authentication/login.html',context)

def registerPage(request):
     

    if request.user.is_authenticated:
          return redirect('home')
     
    else:
          
          form =CreateUserForm()
          if request.method=='POST':
               form=CreateUserForm(request.POST)
               if form.is_valid():
                    form.save()
                    user =form.cleaned_data.get('username')
                    messages.success(request,'Account was created sucessfully for '+user)
                    return redirect('login')
          context={'form':form}
      
          return render(request,'authentication/register.html',context)
    
def notice(request):
    return render(request,'notice/noticeboard.html')
    
def logoutUser(request):
     logout(request)
     return redirect('login')