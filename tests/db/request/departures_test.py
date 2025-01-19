import datetime
import pytest

from pyhafas import HafasClient
from pyhafas.profile import DBProfile


@pytest.mark.skip()
def test_db_departures_request():
    client = HafasClient(DBProfile())
    departures = client.departures(
        station="8011160",
        date=datetime.datetime.now(),
        max_trips=2
    )
    assert len(departures) <= 2
