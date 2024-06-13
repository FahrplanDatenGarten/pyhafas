from pyhafas import HafasClient
from pyhafas.profile import NASAProfile


# Test Location request of NASA by searching for 'Universtitätsbibliothek, Magdeburg', assert that at least one result is returned
def test_locations_request_nasa():
    client = HafasClient(NASAProfile())
    result = client.locations('Halle (Saale) Hbf')
    assert len(result) > 0
