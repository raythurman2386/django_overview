import logging

from django import forms

from .models import Location

logger = logging.getLogger(__name__)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "description", "latitude", "longitude"]

    def clean(self):
        cleaned_data = super().clean()
        logger.debug(f"Cleaning form data: {cleaned_data}")
        return cleaned_data

    def clean_latitude(self):
        latitude = self.cleaned_data.get("latitude")
        if latitude is not None:
            if latitude < -90 or latitude > 90:
                logger.warning(f"Invalid latitude value: {latitude}")
                raise forms.ValidationError(
                    "Latitude must be between -90 and 90 degrees"
                )
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get("longitude")
        if longitude is not None:
            if longitude < -180 or longitude > 180:
                logger.warning(f"Invalid longitude value: {longitude}")
                raise forms.ValidationError(
                    "Longitude must be between -180 and 180 degrees"
                )
        return longitude
