from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Deployable_Pool
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR Password is INCORRECT')
            return render(request, 'login.html')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
   return render(request,'home.html')
