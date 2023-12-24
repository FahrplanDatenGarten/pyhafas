import pytz

from pyhafas.profile.base import BaseProfile
from pyhafas.profile.oebb.requests.journey import OEBBJourneyRequest
from pyhafas.profile.oebb.requests.journeys import OEBBJourneysRequest


class OEBBProfile(OEBBJourneyRequest, OEBBJourneysRequest, BaseProfile):
    """
    Profile of the HaFAS of Österreichische Bundesbahnen (ÖBB) - Austrian Federal Railways - Long-distance and regional trains within Austria
    """

    baseUrl = "https://fahrplan.oebb.at/bin/mgate.exe"

    locale = "de-AT"
    timezone = pytz.timezone("Europe/Vienna")

    requestBody = {
        "client": {
            "id": "OEBB",
            "v": "6030600",
            "type": "IPH",
            "name": "oebbPROD-ADHOC",
        },
        "ext": "OEBB.13",
        "lang": "deu",
        "ver": "1.41",
        "auth": {"type": "AID", "aid": "OWDL4fE4ixNiPBBm"},
    }

    availableProducts = {
        "nationalExpress": [1],  # ICE/RJ
        "national": [2, 4],  # IC/EC
        "interregional": [8, 4096],  # D/EN
        "regional": [16],  # R/REX/CJX
        "suburban": [32],  # S-Bahn
        "bus": [64],  # Bus
        "ferry": [128],  # F
        "subway": [256],  # U
        "tram": [512],  # T
        "onCall": [2048],  # on-call transit, lifts, etc.
    }

    defaultProducts = [
        "nationalExpress",
        "national",
        "interregional",
        "regional",
        "suburban",
        "bus",
        "ferry",
        "subway",
        "tram",
        "onCall",
    ]
