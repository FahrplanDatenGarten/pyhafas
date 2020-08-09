import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey


def test_db_journey_request():
    client = HafasClient(DBProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Siegburg/Bonn@L=8005556@a=128@$A=1@O=Troisdorf@L=8000135@a=128@$202008081507$202008081512$S     19$$1$$$c",
    )
    assert isinstance(journey, Journey)
