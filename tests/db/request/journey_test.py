import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey


def test_db_journey_request():
    client = HafasClient(DBProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Siegburg/Bonn@L=8005556@a=128@$A=1@O=Hennef(Sieg)@L=8002753@a=128@$202106051440$202106051445$S     12$$1$$$",
    )
    assert isinstance(journey, Journey)
