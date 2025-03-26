from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def redirect_to_mapping(request):
    return redirect("location_list")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("mapping/", include("mapping.urls")),
    path("", redirect_to_mapping, name="home"),
]
