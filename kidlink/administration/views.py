from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator
from .models import Activity
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


# adding an activity to the database
def add_activity(request):
    if request.method == "POST":
        activity_name = request.POST.get("activity_name")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        
        Activity.objects.create(
            activity_name = activity_name,
            description = description,
            start_date = start_date,
            end_date = end_date
        )
        return redirect("acitivity_list.html")
    return render(request, "/activites/add_activity.html")

# rendering the list of activities
def list_activites(request):
    activites = Activity.objects.all()
    return render(request, "acitvity_list.html", {"activities":activites})