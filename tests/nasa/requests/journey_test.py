from pyhafas import HafasClient
from pyhafas.profile import NASAProfile
from pyhafas.types.fptf import Journey


# Test journey request with NASA profile
def test_nasa_journey_request():
    client = HafasClient(NASAProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Halle (Saale) Hbf@L=8010159@a=128@$A=1@O=Leipzig Hbf (tief)@L=8098205@a=128@$202312232115$202312232138$ S5X$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#49#AM2#0#RT#15#¶KCC¶I1ZFIzEjRVJHIzEjSElOIzAjRUNLIzE1Njc1fDE1Njc1fDE1Njk4fDE1Njk4fDB8MHw1fDE1Njc1fDF8MHwyfDB8MHwtMjE0NzQ4MzY0OCNHQU0jMjMxMjIzMjExNSMKWiNWTiMxI1NUIzE3MDMyNDY4OTcjUEkjMCNaSSM2MDA0NSNUQSMwI0RBIzIzMTIyMyMxUyM4MDEwMTU5IzFUIzIxMTUjTFMjODAxMDM5NyNMVCMyMjU3I1BVIzgwI1JUIzEjQ0EjcyNaRSNTNVgjWkIjICAgICBTNVgjUEMjNCNGUiM4MDEwMTU5I0ZUIzIxMTUjVE8jODA5ODIwNSNUVCMyMTM4Iw==¶KRCC¶#VE#1#",
    )
    assert isinstance(journey, Journey)
