import pytest

from pyhafas import HafasClient
from pyhafas.profile import DBProfile


@pytest.mark.skip()
def test_db_locations_request():
    client = HafasClient(DBProfile())
    locations = client.locations(term="Köln Messe/Deutz")
    assert len(locations) >= 1
