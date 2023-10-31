import pytz

from pyhafas.profile.base import BaseProfile
from pyhafas.profile.vvv.requests.journey import VVVJourneyRequest
from pyhafas.profile.vvv.requests.journeys import VVVJourneysRequest


class VVVProfile(VVVJourneyRequest, VVVJourneysRequest, BaseProfile):
    """
    Profile of the HaFAS of Verkehrsverbund Vorarlberg (VVV)
    https://de.wikipedia.org/wiki/Verkehrsverbund_Vorarlberg
    """

    baseUrl = "https://fahrplan.vmobil.at/bin/mgate.exe"

    addMicMac = True
    salt = '6633673735743766726667323938336A'

    locale = 'at-DE'
    timezone = pytz.timezone('Europe/Vienna')

    requestBody = {
        "client": {
            "id": "VAO",
            "l": "vs_vvv",
            "name": "webapp",
            "type": "WEB",
            "v": "20230901"
        },
        "ext": "VAO.20",
        "ver": "1.59",
        "lang": "de",
        "auth": {
            "type": "AID",
            "aid": "wf7mcf9bv3nv8g5f"
        }
    }

    availableProducts = {
        'train-and-s-bahn': [1, 2],  # Bahn & S-Bahn
        'u-bahn': [4],  # U-Bahn
        'tram': [16],  # Straßenbahn
        'long-distance-bus': [32],  # Fernbus
        'regional-bus': [64],  # Regionalbus
        'city-bus': [128],  # Stadtbus
        'aerial-lift': [256],  # Seil-/Zahnradbahn
        'ferry': [512],  # Schiff
        'on-call': [1024],  # Anrufsammeltaxi
        'other-bus': [2048]  # sonstige Busse
    }

    defaultProducts = [
        'train-and-s-bahn',
        'u-bahn',
        'tram',
        'long-distance-bus',
        'regional-bus',
        'city-bus',
        'aerial-lift',
        'ferry',
        'on-call',
        'other-bus'
    ]
