from pyhafas import HafasClient
from pyhafas.profile import VSNProfile
from pyhafas.types.fptf import Journey


def test_vsn_journey_request():
    client = HafasClient(VSNProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Lenglern@L=8003644@a=128@$A=1@O=Göttingen@L=4950128@a=128@$202312232144$202312232154$ RB85$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#16433#AM2#0#RT#15#¶KRCC¶#VE#1#",
    )
    assert isinstance(journey, Journey)
