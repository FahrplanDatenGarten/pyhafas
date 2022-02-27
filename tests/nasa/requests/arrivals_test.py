from datetime import datetime

from pyhafas import HafasClient
from pyhafas.profile import NASAProfile


# Test arrivals request for NASAProfile of station 'Universitätsbibliothek' with id '7482'

def test_nasa_arrivals_request():
    client = HafasClient(NASAProfile())
    arrivals = client.arrivals(
        station="7482",
        date=datetime.now(),
        max_trips=5
    )
    assert arrivals
