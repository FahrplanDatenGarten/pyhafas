import os

from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Station

from tests.types import PyTestHafasResponse


def test_oebb_locations_parsing():
    directory = os.path.dirname(os.path.realpath(__file__))
    raw_hafas_json_file = open(directory + "/locations_raw.json", "r")
    hafas_response = PyTestHafasResponse(raw_hafas_json_file.read())
    raw_hafas_json_file.close()
    correct_locations = [
        Station(
            id="1290401",
            lid="A=1@O=Wien Hbf (U)@X=16375326@Y=48185507@U=181@L=1290401@B=1@p=1703147972@",
            name="Wien Hbf (U)",
            latitude=48.185507,
            longitude=16.375326,
        ),
        Station(
            id="1190100",
            lid="A=1@O=Wien@X=16372134@Y=48208547@U=181@L=1190100@B=1@p=1703147972@",
            name="Wien",
            latitude=48.208547,
            longitude=16.372134,
        ),
        Station(
            id="1192101",
            lid="A=1@O=Wien Floridsdorf@X=16400352@Y=48256828@U=181@L=1192101@B=1@p=1703147972@",
            name="Wien Floridsdorf",
            latitude=48.256828,
            longitude=16.400352,
        ),
        Station(
            id="1292101",
            lid="A=1@O=Wien Floridsdorf Bahnhof (U)@X=16400352@Y=48256828@U=181@L=1292101@B=1@p=1703147972@",
            name="Wien Floridsdorf Bahnhof (U)",
            latitude=48.256828,
            longitude=16.400352,
        ),
    ]
    assert OEBBProfile().parse_location_request(hafas_response) == correct_locations
