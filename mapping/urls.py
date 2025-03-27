from django.urls import path

from . import views

urlpatterns = [
    path("", views.location_list, name="location_list"),
    path("add/", views.location_create, name="location_create"),
    path("<int:pk>/edit/", views.location_update, name="location_update"),
    path("<int:pk>/delete/", views.location_delete, name="location_delete"),
]
