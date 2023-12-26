from pyhafas import HafasClient
from pyhafas.profile import OEBBProfile
from pyhafas.types.fptf import Journey


def test_oebb_journey_request():
    client = HafasClient(OEBBProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Neunkirchen NÖ Bahnhof@L=8101277@a=128@$A=1@O=Wr.Neustadt Hbf@L=8100516@a=128@$202312252214$202312252225$CJX 9   $$1$$$$$$¶KRCC¶#VE#1#MRTF#",
    )
    assert isinstance(journey, Journey)
