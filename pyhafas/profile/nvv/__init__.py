import pytz

from pyhafas.profile.base import BaseProfile
from pyhafas.profile.nvv.requests.journey import NVVJourneyRequest
from pyhafas.profile.nvv.requests.journeys import NVVJourneysRequest


class NVVProfile(NVVJourneyRequest, NVVJourneysRequest, BaseProfile):
    """
    Profile for the HaFAs of "Nordhessischer Verkehrs Verbund"
    (NVV) - local transportation provider
    """
    baseUrl = "https://auskunft.nvv.de/bin/mgate.exe"
    defaultUserAgent = "NVV Mobil/5.3.1 (iPhone; IOS 13.1.2; Scale/2.00)"

    addMicMac = False
    addChecksum = False

    locale = "de-DE"
    timezone = pytz.timezone("Europe/Berlin")

    requestBody = {
        "client": {
            "id": "NVV",
            "type": "WEB",
            "name": "webapp"
        },
        "ver": "1.39",
        "lang": "deu",
        "auth":{
            "type": "AID",
            "aid": "R7aKWQLVBRSoVRtY"
        }
    }

    availableProducts = {
        'long_distance_express': [1],   # ICE
        'long_distance': [2],           # IC/EC
        'regional_express': [4],        # RE/RB
        'tram': [32],                   # Tram
        'bus': [64, 128],               # Bus
        'anruf_sammel_taxi': [512],     # Group Taxi
        'regio_tram': [1024]            # Tram / regional express hybrid
    }

    defaultProducts = [
        'long_distance_express',
        'long_distance',
        'regional_express',
        'bus',
        'tram',
        'anruf_sammel_taxi',
        'regio_tram'
    ]
