import datetime
import pytest

from pyhafas import HafasClient
from pyhafas.profile import DBProfile


@pytest.mark.skip()
def test_db_arrivals_request():
    client = HafasClient(DBProfile())
    arrivals = client.arrivals(
        station="8011160",
        date=datetime.datetime.now(),
        max_trips=2
    )
    assert len(arrivals) <= 2
