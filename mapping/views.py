import logging

from django.shortcuts import get_object_or_404, redirect, render

from .forms import LocationForm
from .models import Location

logger = logging.getLogger(__name__)


def location_list(request):
    logger.info(f"Accessing location list view - User: {request.user}")
    try:
        locations = Location.objects.all()
        logger.debug(f"Retrieved {locations.count()} locations from database")
        return render(request, "mapping/location_list.html", {"locations": locations})
    except Exception as e:
        logger.error(f"Error retrieving locations: {str(e)}", exc_info=True)
        raise


def location_create(request):
    logger.info(f"Accessing location create view - User: {request.user}")
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            try:
                location = form.save()
                logger.info(f"Successfully created new location: {location.name}")
                return redirect("location_list")
            except Exception as e:
                logger.error(f"Error creating location: {str(e)}", exc_info=True)
                raise
        else:
            logger.warning(f"Invalid form submission: {form.errors}")
    else:
        form = LocationForm()
        logger.debug("Rendering empty location form")
    return render(request, "mapping/location_form.html", {"form": form})


def location_update(request, pk):
    logger.info(f"Accessing location update view for pk={pk} - User: {request.user}")
    location = get_object_or_404(Location, pk=pk)

    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            try:
                updated_location = form.save()
                logger.info(f"Successfully updated location: {updated_location.name}")
                return redirect("location_list")
            except Exception as e:
                logger.error(
                    f"Error updating location {location.name}: {str(e)}", exc_info=True
                )
                raise
        else:
            logger.warning(
                f"Invalid form submission for location {location.name}: {form.errors}"
            )
    else:
        form = LocationForm(instance=location)
        logger.debug(f"Rendering update form for location: {location.name}")

    return render(
        request, "mapping/location_form.html", {"form": form, "location": location}
    )


def location_delete(request, pk):
    logger.info(f"Accessing location delete view for pk={pk} - User: {request.user}")
    location = get_object_or_404(Location, pk=pk)

    if request.method == "POST":
        try:
            location_name = location.name
            location.delete()
            logger.info(f"Successfully deleted location: {location_name}")
            return redirect("location_list")
        except Exception as e:
            logger.error(
                f"Error deleting location {location.name}: {str(e)}", exc_info=True
            )
            raise

    logger.debug(f"Rendering delete confirmation for location: {location.name}")
    return render(
        request, "mapping/location_confirm_delete.html", {"location": location}
    )
