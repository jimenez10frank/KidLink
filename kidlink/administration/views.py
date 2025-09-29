from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator
# Create your views here.

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                Administrator.objects.get(user=user)
                login(request, user)
                return redirect("admin_dashboard")
            except Administrator.DoesNotExist:
                return render(request, "administration/login.html", {
                    "error": "You are noy registered as an administrator."
                })
        else:
            return render(request, "administration/login.html", {
                "error": "Invalid Username or password."
            })
    return render(request, "administration/login.html")
    
def admin_logout(request):
    logout(request)
    return redirect("admin_login")

@login_required
def admin_dashboard(request):
    return render(request, "administration/dashboard.html")
