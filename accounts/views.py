from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import (
    LoginForm,
    RegisterForm
)

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect("/login")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        # verify valid username / password

        user = authenticate(username=username, password=password)
        if user == None:
            print("User is invalid")
            # later add a message
            return redirect("/login")
        # perform login
        # print(user.username)
        login(request, user)
        # redirect to a logged in required page
        return redirect("/")
    return render(request, "accounts/login.html", {"form":form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user_obj.is_active = False
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()
        return redirect("/login")
        print(form.cleaned_data, user_obj)
    return render(request, "accounts/register.html", {"form": form})