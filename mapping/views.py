from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location


def location_list(request):
    locations = Location.objects.all()
    return render(request, "mapping/location_list.html", {"locations": locations})


def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("location_list")
    else:
        form = LocationForm()
    return render(request, "mapping/location_form.html", {"form": form})
