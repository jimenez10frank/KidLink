from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("youth/", views.youth_list, name="youth_list"),
    path("youth/add/", views.youth_create, name="youth_create"),
    path("youth/<int:pk>/edit/", views.youth_update, name="youth_update"),
    path("youth/<int:pk>/delete/", views.youth_delete, name="youth_delete"),

]
