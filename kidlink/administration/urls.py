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
    path("youth/activities/", views.youth_activity_list, name="youth_activity_list"),
    path("youth/activities/add/", views.youth_activity_create, name="youth_activity_create"),
    path("youth/activities/<int:pk>/edit/", views.youth_activity_update, name="youth_activity_update"),
    path("youth/activities/<int:pk>/delete/", views.youth_activity_delete, name="youth_activity_delete"),
    #activities urls
    path("activities/", views.activity_list, name="activity_list"),
    path("activities/add/", views.add_activity, name="add_activity"),
    path("activities/<int:pk>/activity_edit/", views.update_activity, name="update_activity"),
    path("activities/<int:pk>/delete_activity/", views.delete_activity, name="delete_activity"),
    #institutes URLS
    path("institutes/", views.institute_list, name="institute_list"),
    path("institutes/add/", views.add_institute, name="add_institute"),
    path("institutes/<int:pk>/institute_edit/", views.update_institute, name="update_institute"),
    path("institutes/<int:pk>/delete_institute/", views.delete_institute, name="delete_institute"),
    #youth institute URLs
    path("youth/institutes/", views.youth_institute_list, name="youth_institute_list"),
    path("youth/institutes/add/", views.youth_institute_create, name="youth_institute_create"),
    path("youth/institutes/<int:pk>/edit/", views.youth_institute_update, name="youth_institute_update"),
    path("youth/institutes/<int:pk>/delete/", views.youth_institute_delete, name="youth_institute_delete"),
]
