from math import radians, sin, cos, sqrt, atan2


def calculate_distance_in_meters(ilat1: float, ilon1: float, ilat2: float, ilon2: float) -> float:
    # credits to https://stackoverflow.com/a/19412565/237312
    # used to not import external libs

    # Approximate radius of earth in meters
    r = 6373000.0

    lat1 = radians(ilat1)
    lon1 = radians(ilon1)
    lat2 = radians(ilat2)
    lon2 = radians(ilon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c

    return distance
