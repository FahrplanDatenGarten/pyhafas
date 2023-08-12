from pyhafas import HafasClient
from pyhafas.profile import NVVProfile
from pyhafas.types.fptf import Journey


def test_nvv_journey_request():
    client = HafasClient(NVVProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Rotenburg (Fulda) Bahnhof@L=2202508@a=128@$A=1@O=Kassel Hauptbahnhof@L=2200001@a=128@$202307050837$202307050921$ RE5$$1$$$$$$¶KRCC¶#VE#1#¶PC¶eyJncnBJZCI6IkdST1VQX1BUIn0="
    )
    assert isinstance(journey, Journey)
