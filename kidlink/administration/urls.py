from django.urls import path
from . import views

urlpatterns = [
    # Administration URLs
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    #activites route
    path("activities/",views.list_activites, name="list_activites"),
    path("activites/add_activity.html", views.add_activity, name="add_activity")
]
