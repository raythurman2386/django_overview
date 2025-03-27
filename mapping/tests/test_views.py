from django.test import Client, TestCase
from django.urls import reverse

from ..forms import LocationForm
from ..models import Location


class LocationViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.location_data = {
            "name": "Test Location",
            "description": "A test location",
            "latitude": 32.7767,
            "longitude": -96.7970,
        }
        self.location = Location.objects.create(**self.location_data)

    def test_location_list_view(self):
        """Test the location list view."""
        response = self.client.get(reverse("location_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mapping/location_list.html")
        self.assertIn("locations", response.context)
        self.assertEqual(list(response.context["locations"]), [self.location])

    def test_location_create_view_get(self):
        """Test the location create view GET request."""
        response = self.client.get(reverse("location_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mapping/location_form.html")
        self.assertIsInstance(response.context["form"], LocationForm)

    def test_location_create_view_post(self):
        """Test the location create view POST request."""
        new_location_data = {
            "name": "New Location",
            "description": "A new location",
            "latitude": 32.7767,
            "longitude": -96.7970,
        }
        response = self.client.post(reverse("location_create"), new_location_data)
        self.assertRedirects(response, reverse("location_list"))
        self.assertEqual(Location.objects.count(), 2)  # Original + new location

    def test_location_update_view_get(self):
        """Test the location update view GET request."""
        response = self.client.get(reverse("location_update", args=[self.location.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mapping/location_form.html")
        self.assertEqual(response.context["location"], self.location)
        self.assertEqual(response.context["form"].instance, self.location)

    def test_location_update_view_post(self):
        """Test the location update view POST request."""
        updated_data = self.location_data.copy()
        updated_data["name"] = "Updated Location"
        response = self.client.post(
            reverse("location_update", args=[self.location.pk]), updated_data
        )
        self.assertRedirects(response, reverse("location_list"))
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "Updated Location")

    def test_location_delete_view_get(self):
        """Test the location delete view GET request."""
        response = self.client.get(reverse("location_delete", args=[self.location.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "mapping/location_confirm_delete.html")
        self.assertEqual(response.context["location"], self.location)

    def test_location_delete_view_post(self):
        """Test the location delete view POST request."""
        response = self.client.post(reverse("location_delete", args=[self.location.pk]))
        self.assertRedirects(response, reverse("location_list"))
        self.assertEqual(Location.objects.count(), 0)

    def test_location_delete_nonexistent(self):
        """Test deleting a nonexistent location."""
        response = self.client.post(reverse("location_delete", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_location_update_nonexistent(self):
        """Test updating a nonexistent location."""
        response = self.client.get(reverse("location_update", args=[999]))
        self.assertEqual(response.status_code, 404)
