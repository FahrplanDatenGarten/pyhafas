import datetime

from pyhafas import HafasClient
from pyhafas.profile import NVVProfile
from pyhafas.types.fptf import Journey


def test_nvv_journey_request():
    profile = NVVProfile()
    today = datetime.datetime.now(datetime.UTC)
    start = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d2105')
    end = profile.transform_datetime_parameter_timezone(today).strftime('%Y%m%d2142')
    client = HafasClient(profile)
    journey = client.journey(
        journey=f"¶HKI¶T$A=1@O=Rotenburg (Fulda) Bahnhof@L=2202508@a=128@$A=1@O=Kassel Bahnhof Wilhelmshöhe@L=2200007@a=128@${start}${end}$ RB5$$1$$$$$$¶KC¶#VE#2#CF#100#CA#0#CM#0#SICT#0#AM#49#AM2#0#RT#7#¶KRCC¶#VE#1#¶PC¶eyJncnBJZCI6IkdST1VQX1BUIn0="
    )
    assert isinstance(journey, Journey)
