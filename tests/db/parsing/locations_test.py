import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Station

from tests.types import PyTestHafasResponse


def test_db_locations_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/locations_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_locations = [
        Station(
            id='008000207',
            name='Köln Hbf',
            latitude=50.942823,
            longitude=6.959197
        ), Station(
            id="008096022",
            name='KÖLN',
            latitude=50.941312,
            longitude=6.967206)
    ]
    assert DBProfile().parse_location_request(hafas_response) == correct_locations
