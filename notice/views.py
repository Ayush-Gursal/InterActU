from django.shortcuts import render
from django.contrib.auth import logout
from .models import *

# Create your views here.


def notice(request):
    x=Notice.objects.all()
    return render(request,'notice/noticeboard.html',{'x':x})

def store(request):
    return render(request,'store/store.html')

def home(request):
    return render(request,'home/home.html')

def rental(request):
    return render(request,'rental/blog.html')

def logout(request):
     logout(request)
     return redirect('logout')
