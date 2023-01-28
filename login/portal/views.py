from django.shortcuts import render,redirect
from .forms import *
from django import contrib 
from django.contrib import messages
import requests

from django.contrib.auth.decorators import login_required 
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created Suceesfully for {username}!!!")
            return redirect('login')
    else:
        form = UserCreationForm()
        context = {
            'form': form 
        }
    return render(request,'register.html',context)

def about(request):
    return render(request,'about.html')

def contactUs(request):
    return render(request,'contactUs.html')