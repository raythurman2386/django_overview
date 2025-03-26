from django.urls import path

from . import views

urlpatterns = [
    path("", views.location_list, name="location_list"),
    path("add/", views.location_create, name="location_create"),
]
