from pyhafas import HafasClient
from pyhafas.profile import VVVProfile
from pyhafas.types.fptf import Journey


def test_vvv_journey_request():
    client = HafasClient(VVVProfile())
    journey = client.journey(
        journey='¶HKI¶G@F$A=2@O=Adlergasse, 6850 Dornbirn@X=9733124@Y=47401432@b=980000657@a=128@$A=1@O=Dornbirn Bäumlegasse@L=480150302@a=128@$202311010129$202311010138')
    assert isinstance(journey, Journey)
