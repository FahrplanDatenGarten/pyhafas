import datetime

from pyhafas import HafasClient
from pyhafas.profile import VVVProfile
from pyhafas.types.fptf import Journey


def test_vvv_journey_request():
    profile = VVVProfile()
    today = datetime.datetime.now(datetime.UTC)
    start = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d0129')
    end = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d0138')
    client = HafasClient(profile)
    journey = client.journey(
        journey=f"¶HKI¶G@F$A=2@O=Adlergasse, 6850 Dornbirn@X=9733124@Y=47401432@b=980000657@a=128@$A=1@O=Dornbirn Bäumlegasse@L=480150302@a=128@${start}${end}"
    )
    assert isinstance(journey, Journey)
