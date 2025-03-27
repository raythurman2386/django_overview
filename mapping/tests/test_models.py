from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Location


class LocationModelTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.location_data = {
            "name": "Test Location",
            "description": "A test location",
            "latitude": 32.7767,
            "longitude": -96.7970,
        }
        self.location = Location.objects.create(**self.location_data)

    def test_location_creation(self):
        """Test that a location can be created with valid data."""
        self.assertEqual(self.location.name, self.location_data["name"])
        self.assertEqual(self.location.description, self.location_data["description"])
        self.assertEqual(self.location.latitude, self.location_data["latitude"])
        self.assertEqual(self.location.longitude, self.location_data["longitude"])

    def test_location_string_representation(self):
        """Test the string representation of a location."""
        self.assertEqual(str(self.location), self.location_data["name"])

    def test_location_validation(self):
        """Test location validation for invalid coordinates."""
        # Test invalid latitude
        with self.assertRaises(ValidationError):
            location = Location(
                name="Invalid Location",
                latitude=91.0,  # Invalid latitude
                longitude=-96.7970,
            )
            location.full_clean()

        # Test invalid longitude
        with self.assertRaises(ValidationError):
            location = Location(
                name="Invalid Location",
                latitude=32.7767,
                longitude=181.0,  # Invalid longitude
            )
            location.full_clean()

    def test_location_ordering(self):
        """Test that locations are ordered by name."""
        Location.objects.create(name="A Location", latitude=32.7767, longitude=-96.7970)
        Location.objects.create(name="B Location", latitude=32.7767, longitude=-96.7970)
        Location.objects.create(name="C Location", latitude=32.7767, longitude=-96.7970)

        locations = Location.objects.all()
        self.assertEqual(locations[0].name, "A Location")
        self.assertEqual(locations[1].name, "B Location")
        self.assertEqual(locations[2].name, "C Location")
