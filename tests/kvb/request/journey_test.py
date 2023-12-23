from pyhafas import HafasClient
from pyhafas.profile import KVBProfile
from pyhafas.types.fptf import Journey


def test_kvb_journey_request():
    client = HafasClient(KVBProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Köln Hbf@L=300000809@a=128@$A=1@O=Köln Ehrenfeld Bf Ehrenfeld@L=300083507@a=128@$202312232115$202312232120$  RE1RRX$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#49#AM2#0#AT0AN#ZP##RT#8#¶KRCC¶#VE#1#IST#¶PC¶eyJncnBJZCI6IlJRX0NMSUVOVCJ9"
    )
    assert isinstance(journey, Journey)
