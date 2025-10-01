from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator, Youth, YouthActivity, Activity
from .forms import YouthForm, YouthActivityForm, ActivityForm
from django.http import HttpResponseForbidden
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



#funtion for adding activity 
@login_required
def add_activity(request):
    if not request.user.is_staff:  # restrict to admins
        return HttpResponseForbidden("You are not authorized to add activities.")

    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("activity_list")
    else:
        form = ActivityForm()
    return render(request, "activities/add_activity.html", {"form": form})

# funtion to show the activity lists
def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activities/activity_list.html', {"activities":activities})

# function to edit an activity
@login_required
def update_activity(request,pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to edit activities")
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
        return render(request, 'activities/activity_update.html',{'form':form})
    
# function to delete an acitivty
@login_required
def delete_activity(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to delete an activity")
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        activity.delete() # deleting  the activity
        return redirect('activity_list') 
    return render(request, 'activities/activity_confirm_delete.html', {'activity': activity})

# Youth Activity Administration
@login_required
def youth_activity_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to view this page.")
    activities = YouthActivity.objects.all()
    return render(request, 'administration/youth_activity_list.html', {'activities': activities})

@login_required
def youth_activity_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to add activities.")
    if request.method == "POST":
        form = YouthActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('youth_activity_list')
    else:
        form = YouthActivityForm()
    return render(request, 'administration/youth_activity_create.html', {'form': form})

@login_required
def youth_activity_update(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to edit activities.")
    activity = get_object_or_404(YouthActivity, pk=pk)
    if request.method == "POST":
        form = YouthActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('youth_activity_list')
    else:
        form = YouthActivityForm(instance=activity)
    return render(request, 'administration/youth_activity_form.html', {'form': form})

@login_required
def youth_activity_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to delete activities.")
    activity = get_object_or_404(YouthActivity, pk=pk)
    if request.method == "POST":
        activity.delete()
        return redirect('youth_activity_list')
    return render(request, 'administration/youth_activity_confirm_delete.html', {'activity': activity})


# LOLLLLLLLLLLL
# Youth Administration
@login_required
def youth_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to view this page.")
    youths = Youth.objects.all()
    return render(request, 'administration/youth_list.html', {'youths': youths})

# for creating Youth
@login_required
def youth_create(request):
    if not request.user.is_staff:  # restrict to admins
        return HttpResponseForbidden("You are not authorized to add youths.")
    if request.method == "POST":
        form = YouthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('youth_list')
    else:
        form = YouthForm()
    return render(request, 'administration/youth_form.html', {'form': form})

# for updating youth
@login_required
def youth_update(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to edit youths.")
    youth = get_object_or_404(Youth, pk=pk)
    if request.method == "POST":
        form = YouthForm(request.POST, instance=youth)
        if form.is_valid():
            form.save()
            return redirect('youth_list')
    else:
        form = YouthForm(instance=youth)
    return render(request,'administration/youth_form.html', {'form': form})

# delete youth
@login_required
def youth_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to delete youths.")
    youth = get_object_or_404(Youth, pk=pk)
    if request.method == "POST":
        youth.delete()
        return redirect('youth_list')
    return render(request, 'administration/youth_confirm_delete.html', {'youth': youth})