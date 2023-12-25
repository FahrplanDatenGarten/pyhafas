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
        "highspeed": [1],  # RJ/RJX/ICE
        "eurocity-intercity": [2, 4],  # EC/IC
        "durchgang-euronight": [8, 4096],  # D/EN
        "regional": [16],  # R/REX/CJX
        "s-bahn": [32],  # S-Bahn
        "bus": [64],  # Bus
        "ferry": [128],  # Schiff
        "u-bahn": [256],  # U-Bahn
        "tram": [512],  # Straßenbahn
        "on-call": [2048],  # on-call transit, lifts, etc.
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
