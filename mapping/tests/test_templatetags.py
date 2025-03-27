from django.test import TestCase

from ..templatetags.location_tags import format_coordinates


class LocationTemplateTagsTest(TestCase):
    def test_format_coordinates(self):
        """Test the format_coordinates template tag."""
        # Test Dallas coordinates
        self.assertEqual(
            format_coordinates(32.7767, -96.7970), "32°46'36\"N, 96°47'49\"W"
        )

        # Test coordinates with zero values
        self.assertEqual(format_coordinates(0.0, 0.0), "0°0'0\"N, 0°0'0\"E")

        # Test coordinates with negative values
        self.assertEqual(
            format_coordinates(-33.8688, 151.2093), "33°52'7\"S, 151°12'33\"E"
        )

        # Test coordinates with decimal values
        self.assertEqual(
            format_coordinates(40.7128, -74.0060), "40°42'46\"N, 74°0'21\"W"
        )
