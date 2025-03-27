from django.test import TestCase

from ..forms import LocationForm
from ..models import Location


class LocationFormTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.valid_data = {
            "name": "Test Location",
            "description": "A test location",
            "latitude": 32.7767,
            "longitude": -96.7970,
        }

    def test_valid_form(self):
        """Test form with valid data."""
        form = LocationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_latitude(self):
        """Test form with invalid latitude."""
        data = self.valid_data.copy()
        data["latitude"] = 91.0
        form = LocationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("latitude", form.errors)

    def test_invalid_longitude(self):
        """Test form with invalid longitude."""
        data = self.valid_data.copy()
        data["longitude"] = 181.0
        form = LocationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("longitude", form.errors)

    def test_empty_name(self):
        """Test form with empty name."""
        data = self.valid_data.copy()
        data["name"] = ""
        form = LocationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_form_save(self):
        """Test form save method."""
        form = LocationForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        location = form.save()
        self.assertEqual(location.name, self.valid_data["name"])
        self.assertEqual(location.description, self.valid_data["description"])
        self.assertEqual(location.latitude, self.valid_data["latitude"])
        self.assertEqual(location.longitude, self.valid_data["longitude"])

    def test_form_update(self):
        """Test form update with existing instance."""
        location = Location.objects.create(**self.valid_data)
        updated_data = self.valid_data.copy()
        updated_data["name"] = "Updated Location"
        form = LocationForm(data=updated_data, instance=location)
        self.assertTrue(form.is_valid())
        updated_location = form.save()
        self.assertEqual(updated_location.name, "Updated Location")
        self.assertEqual(updated_location.pk, location.pk)
