from django import template

register = template.Library()


@register.filter
def format_latitude(value):
    """
    Format latitude with N/S hemisphere.
    Example: 40.7128 becomes 40.71° N
    """
    try:
        float_value = float(value)
        direction = "N" if float_value >= 0 else "S"
        return f"{abs(float_value):.2f}° {direction}"
    except (ValueError, TypeError):
        return value


@register.filter
def format_longitude(value):
    """
    Format longitude with E/W hemisphere.
    Example: -74.0060 becomes 74.01° W
    """
    try:
        float_value = float(value)
        direction = "E" if float_value >= 0 else "W"
        return f"{abs(float_value):.2f}° {direction}"
    except (ValueError, TypeError):
        return value


@register.simple_tag
def format_coordinates(latitude, longitude):
    """
    Format both latitude and longitude together.
    Example: (40.7128, -74.0060) becomes 40.71° N, 74.01° W
    """
    lat_str = format_latitude(latitude)
    lng_str = format_longitude(longitude)
    return f"{lat_str}, {lng_str}"
