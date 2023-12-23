from pyhafas import HafasClient
from pyhafas.profile import NVVProfile
from pyhafas.types.fptf import Journey


def test_nvv_journey_request():
    client = HafasClient(NVVProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Rotenburg (Fulda) Bahnhof@L=2202508@a=128@$A=1@O=Kassel Bahnhof Wilhelmshöhe@L=2200007@a=128@$202312232105$202312232142$ RB5$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#49#AM2#0#RT#7#¶KRCC¶#VE#1#¶PC¶eyJncnBJZCI6IkdST1VQX1BUIn0="
    )
    assert isinstance(journey, Journey)
