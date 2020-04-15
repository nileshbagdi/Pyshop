from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import products, offers,Deployable_Pool
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

def register(request):
    form=UserCreationForm()

    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'Signup.html',{'form':form})

@login_required(login_url='login')
def index(request):
    #Product=products.objects.all()
    return render(request,'home.html')


@login_required(login_url='login')
def new(request):
    Offers=offers.objects.all()
    return render(request,'offers.html',{'Offers':Offers})

@login_required(login_url='login')
def dp(request):
    dp_data=Deployable_Pool.objects.all()
    return render(request,'dp.html',{'dp_data':dp_data})
