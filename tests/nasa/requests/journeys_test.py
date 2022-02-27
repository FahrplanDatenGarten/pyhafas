from datetime import datetime
from pyhafas import HafasClient
from pyhafas.profile import NASAProfile


# Test journeys of NASA profile with a trip from 'Universitätsbibliothek' (id: 7482) to 'Neue Str./Zirkusmuseum' (id: 7411)
def test_nasa_journeys():
    client = HafasClient(profile=NASAProfile())
    journeys = client.journeys(
        origin='7482',
        destination='7411',
        date=datetime.now(),
        min_change_time=0,
        max_changes=-1
    )
    assert journeys