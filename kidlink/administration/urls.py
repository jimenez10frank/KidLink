from django.urls import path
from . import views

urlpatterns = [
    # Administration URLs
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("dashboard/", views.admin_dashboard, name="admin_dashboard"),
    # Youth Management URLs
    path("youth/", views.youth_list, name="youth_list"),
    path("youth/add/", views.youth_create, name="youth_create"),
    path("youth/<int:pk>/edit/", views.youth_update, name="youth_update"),
    path("youth/<int:pk>/delete/", views.youth_delete, name="youth_delete"),
    # youth activities URLs
    path("youth/<int:pk>/activities/", views.activity_list, name="activity_list"),
    path("youth/<int:pk>/activities/add/", views.activity_create, name="activity_create"),
    path("youth/<int:pk>/activities/<int:activity_pk>/edit/", views.activity_update, name="activity_update"),
    path("youth/<int:pk>/activities/<int:activity_pk>/delete/", views.activity_delete, name="activity_delete"),
    #activities urls

]
