import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey


def test_db_departures_request():
    client = HafasClient(DBProfile())
    locations = client.locations(term="Köln Messe/Deutz")
    assert len(locations) >= 1
