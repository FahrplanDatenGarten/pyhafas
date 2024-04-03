import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile
from pyhafas.types.fptf import Journey


def test_db_journey_request():
    profile = DBProfile()
    today = datetime.datetime.now(datetime.UTC)
    start = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d1439')
    end = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d1445')
    client = HafasClient(profile)
    journey = client.journey(
        journey=f"¶HKI¶T$A=1@O=Siegburg/Bonn@L=8005556@a=128@$A=1@O=Hennef(Sieg)@L=8002753@a=128@${start}${end}$S     12$$1$$$",
    )
    assert isinstance(journey, Journey)
