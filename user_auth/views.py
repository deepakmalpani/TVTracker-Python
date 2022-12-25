from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm

# Create your views here.
def create_new_user(request):
    if request.user.is_authenticated:
        return redirect("home")

    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("user_auth:login")
        
        form = CreateUserForm()
        context = {"form" : form}
        return render(request,'authentication/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            form = AuthenticationForm()
            context = {'form' : form}
            return render(request,'authentication/login.html', context)
    else:
        form = AuthenticationForm()
        context = {'form' : form}
        return render(request,'authentication/login.html', context)

def logout_user(request):
    logout(request)
    return redirect("user_auth:login")