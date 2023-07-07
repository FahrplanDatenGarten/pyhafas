from pyhafas import HafasClient
from pyhafas.profile import NASAProfile
from pyhafas.types.fptf import Journey


# Test journey request with NASA profile
def test_nasa_journey_request():
    client = HafasClient(NASAProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Magdeburg, Universitätsbibliothek@L=300748202@a=128@$A=1@O=Magdeburg, Opernhaus@L=300737002@a=128@$202307071925$202307071929$Str    2$$1$$$$$$§T$A=1@O=Magdeburg, Opernhaus@L=300737002@a=128@$A=1@O=Magdeburg, Arndtstr.@L=300731502@a=128@$202307071932$202307071944$Str    1$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#49#AM2#0#RT#7#¶KCC¶I1ZFIzEjRVJHIzIjSElOIzAjRUNLIzE0MTI1fDE0MTI1fDE0MTQ0fDE0MTQ0fDB8MHw4NXwxNDExM3wxfDB8MnwwfDB8LTIxNDc0ODM2NDgjR0FNIzcwNzIzMTkyNSMKWiNWTiMxI1NUIzE2ODg3MTM3MTUjUEkjMCNaSSMzNjM0I1RBIzMjREEjNzA3MjMjMVMjMzAwNzQ3ODAyIzFUIzE5MTkjTFMjMzAwNzU0MDAzI0xUIzE5NTkjUFUjODAjUlQjMSNDQSNTdE4jWkUjMiNaQiNTdHIgICAgMiNQQyM1I0ZSIzMwMDc0ODIwMiNGVCMxOTI1I1RPIzMwMDczNzAwMiNUVCMxOTI5IwpaI1ZOIzEjU1QjMTY4ODcxMzcxNSNQSSMwI1pJIzM0MzAjVEEjMyNEQSM3MDcyMyMxUyMzMDA3Mzg2MDEjMVQjMTkxNiNMUyMzMDA3MzE0MDIjTFQjMTk0NSNQVSM4MCNSVCMxI0NBI1N0TiNaRSMxI1pCI1N0ciAgICAxI1BDIzUjRlIjMzAwNzM3MDAyI0ZUIzE5MzIjVE8jMzAwNzMxNTAyI1RUIzE5NDQj¶KRCC¶#VE#1#",
    )
    assert isinstance(journey, Journey)
