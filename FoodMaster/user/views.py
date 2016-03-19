from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login

from FoodMaster.portion.models import Portion


# Create your views here.
def register(request):
    if request.method == "POST":
        #register user
        User.objects.create_user(username=request.POST.get("username"),
                                 password=request.POST.get("password"),
                                 first_name=request.POST.get("first_name"),
                                 last_name=request.POST.get("last_name"))

        return render(request, "user/register.html", {"message": "Your registration is successful!"})

    return render(request, "user/register.html", {})

def login(request):
    if request.method == "POST":
        message = ""
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"))

        if user:
            auth_login(request, user)
            # message = "Welcome, nerdy birdy!"
        else:
            message = "Something went wrong!"
            return render(request, "user/login.html", {"message": message})

        return redirect('home')

    return render(request, "user/login.html", {})

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    # This what we do on Home page
    message = "Hello, {name}!"
    user = request.user

    if user.is_authenticated():
        name = user.first_name
    else:
        name = "stranger"

    message = message.format(name=name)
    return render(request, "home.html", {"greeting_message": message})

def profile(request, username):
    portions = list(Portion.objects.filter(user__username=username).select_related())
    user = portions[0].user

    return render(request, "user/profile.html", {"user": user, "portions": portions})

