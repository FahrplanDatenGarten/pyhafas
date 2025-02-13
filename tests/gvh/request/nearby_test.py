from pyhafas import HafasClient
from pyhafas.profile.gvh import GVHProfile
from pyhafas.types.nearby import LatLng
from tests.distance import calculate_distance_in_meters


def test_gvh_nearby_request():
    pos = LatLng(50.940614, 6.958120)
    client = HafasClient(GVHProfile())
    stations = client.nearby(pos)
    assert stations
    assert calculate_distance_in_meters(pos.latitude, pos.longitude, stations[0].latitude, stations[0].longitude) < 200
