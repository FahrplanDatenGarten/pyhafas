from pyhafas import HafasClient
from pyhafas.profile import VSNProfile
from pyhafas.types.fptf import Journey


def test_vsn_departures_request():
    client = HafasClient(VSNProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Göttingen@L=8000128@a=128@$A=1@O=Lenglern@L=8003644@a=128@$202008090710$202008090719$    RB85$$1$$$",
    )
    assert isinstance(journey, Journey)
