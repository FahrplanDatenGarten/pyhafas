from pyhafas import HafasClient
from pyhafas.profile import KVBProfile
from pyhafas.types.fptf import Journey


def test_kvb_journey_request():
    client = HafasClient(KVBProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Köln Mülheim Keupstr.@L=300063102@a=128@$A=1@O=Köln Mülheim Grünstr.@L=300056802@a=128@$202305250936$202305250939$ 4$$1$$$$"
    )
    assert isinstance(journey, Journey)
