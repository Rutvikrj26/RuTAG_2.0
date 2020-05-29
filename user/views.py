from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        messages.info(request, "You have successfully registered!!!")

        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Username or Password Incorrect")
            return render(request, "login.html", context)

        messages.success(request, "You have successfully Logged In")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "You have successfully Logged Out")
    return redirect("index")


def Events(request):
    return render(request, "Events.html")


def Publications(request):
    return render(request, "Publications.html")


def Projects(request):
    return render(request, "Projects.html")


def IPD(request):
    return render(request, "IPD.html")


def News(request):
    return render(request, "News.html")


def Collaborators(request):
    return render(request, "Collaborators.html")


def Conferences(request):
    return render(request, "Conferences.html")


def RuTAG_Club(request):
    return render(request, "RuTAG_Club.html")
