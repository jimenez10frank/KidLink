from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("activities/", views.activity_list, name="acitivity_list"),
    path("activities/add", views.add_activity, name="add_activity")
]
