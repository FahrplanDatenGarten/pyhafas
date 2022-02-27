from pyhafas import HafasClient
from pyhafas.profile import NASAProfile
from pyhafas.types.fptf import Journey


# Test journey request with NASA profile
def test_nasa_journey_request():
    client = HafasClient(NASAProfile())
    journey = client.journey(
        journey="¶HKI¶T$A=1@O=Magdeburg, Universitätsbibliothek@L=7482@a=128@$A=1@O=Magdeburg, Neue Str./Zirkusmuseum@L=7411@a=128@$202202271954$202202272011$Str    2$$1$$$$¶KCC¶I1ZFIzEjRVJHIzEjSElOIzAjRUNLIzE4NDc0fDE4NDc0fDE4NDkxfDE4NDkxfDB8MHw1fDE4NDYxfDF8LTIxNDc0ODM2NDZ8MCNHQU0jMjcwMjIyMTk1NCMKWiNWTiMxI1NUIzE2NDU3ODQ5NjEjUEkjMCNaSSMyMzg3I1RBIzQjREEjMjcwMjIyIzFTIzc0NzgjMVQjMTk0OCNMUyM3NTQwI0xUIzIwMjYjUFUjODAjUlQjMSNDQSNTdE4jWkUjMiNaQiNTdHIgICAgMiNQQyM1I0ZSIzc0ODIjRlQjMTk1NCNUTyM3NDExI1RUIzIwMTEj",
    )
    assert isinstance(journey, Journey)
