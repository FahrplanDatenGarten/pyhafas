import os

from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Station

from tests.types import PyTestHafasResponse


def test_db_locations_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/locations_raw.json", "r", encoding="utf8")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_locations = [
        Station(
            id='008000207',
            lid='A=1@O=Köln Hbf@X=6958730@Y=50943029@U=80@L=008000207@B=1@p=1596188796@',
            name='Köln Hbf',
            latitude=50.942823,
            longitude=6.959197
        ), Station(
            id="008096022",
            lid='A=1@O=KÖLN@X=6967206@Y=50941312@U=80@L=008096022@B=1@p=1596188796@',
            name='KÖLN',
            latitude=50.941312,
            longitude=6.967206)
    ]
    assert DBProfile().parse_location_request(hafas_response) == correct_locations
