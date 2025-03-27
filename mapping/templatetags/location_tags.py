from django import template

register = template.Library()


def decimal_to_dms(decimal_degrees):
    """Convert decimal degrees to degrees, minutes, seconds."""
    degrees = int(abs(decimal_degrees))
    minutes_decimal = (abs(decimal_degrees) - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = int((minutes_decimal - minutes) * 60)
    return degrees, minutes, seconds


@register.filter
def format_latitude(value):
    """
    Format latitude with N/S hemisphere.
    Example: 40.7128 becomes 40°42'46"N
    """
    try:
        float_value = float(value)
        direction = "N" if float_value >= 0 else "S"
        degrees, minutes, seconds = decimal_to_dms(float_value)
        return f"{degrees}°{minutes}'{seconds}\"{direction}"
    except (ValueError, TypeError):
        return value


@register.filter
def format_longitude(value):
    """
    Format longitude with E/W hemisphere.
    Example: -74.0060 becomes 74°0'22"W
    """
    try:
        float_value = float(value)
        direction = "E" if float_value >= 0 else "W"
        degrees, minutes, seconds = decimal_to_dms(float_value)
        return f"{degrees}°{minutes}'{seconds}\"{direction}"
    except (ValueError, TypeError):
        return value


@register.simple_tag
def format_coordinates(latitude, longitude):
    """
    Format both latitude and longitude together.
    Example: (40.7128, -74.0060) becomes 40°42'46"N, 74°0'22"W
    """
    lat_str = format_latitude(latitude)
    lng_str = format_longitude(longitude)
    return f"{lat_str}, {lng_str}"
