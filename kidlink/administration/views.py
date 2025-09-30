from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator
from .models import Activities
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


#funtion for adding activity 
def add_activity(request):
    if request.method == "POST":
        acitivity_name = request.POST.get('activity_name')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        location = request.POST.get('location')
        
    # Saving this to the database
        Activities.objects.create(
            acitivity_name = acitivity_name,
            description = description,
            start_date = start_date,
            end_date = end_date,
            location = location
        )
    
        return redirect("activity_list")
    return render(request, "add_activity.html")

# funtion to show the activity lists
def activity_list(request):
    activities = Activities.objects.all()
    return render(request, 'activities/activity_list.html', {"activities":activities})

    
        