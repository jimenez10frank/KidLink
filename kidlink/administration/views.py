from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Administrator, Youth, YouthActivity
from .forms import YouthForm
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

# Youth Activities Views
@login_required
def youth_activity_list(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to view this page.")
    youth = get_object_or_404(Youth, pk=pk)
    activities = YouthActivity.objects.filter(youth=youth)
    return render(request, 'administration/youth_activity_list.html', {'youth': youth, 'activities': activities})