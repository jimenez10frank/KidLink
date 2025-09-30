from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator
# Create your views here.

# administration Authentication
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # only staff can log in
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "administration/login.html", {
                "error": "Invalid credentials or not an administrator."
            })
    return render(request, "administration/login.html")


    
def admin_logout(request):
    logout(request)
    return redirect("admin_login")

@login_required
def admin_dashboard(request):
    return render(request, "administration/dashboard.html")
