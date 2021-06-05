from pyhafas import HafasClient
from pyhafas.profile import VSNProfile
from pyhafas.types.fptf import Journey


def test_vsn_journey_request():
    client = HafasClient(VSNProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Lenglern Bahnhof@L=9909403@a=128@$A=1@O=Göttingen Bahnhof/ZOB@L=1101000@a=128@$202106051527$202106051550$Bus 220 $$1$$$$",
    )
    assert isinstance(journey, Journey)
