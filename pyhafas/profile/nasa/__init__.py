import pytz

from pyhafas.profile.base import BaseProfile
from pyhafas.profile.nasa.requests.journeys import NASAJourneysRequest
from pyhafas.profile.nasa.requests.journey import NASAJourneyRequest


class NASAProfile(NASAJourneyRequest, NASAJourneysRequest, BaseProfile):
    """
    Profile of the HaFAS of NASA (Nahverkehr Sachsen-Anhalt).
    """

    baseUrl = "https://reiseauskunft.insa.de/bin/mgate.exe"
    defaultUserAgent = "Dalvik/2.1.0 (Linux; U; Android 11; Pixel 4a Build/RQ2A.210305.006)"

    addMicMac = False
    addChecksum = False

    locale = 'de-DE'
    timezone = pytz.timezone('Europe/Berlin')

    requestBody = {
        "client": {
            "id": "NASA",
            "type": "IPH",
            "name": "nasaProd",
            "v": "4000200",
        },
        "ver": "1.44",
        "lang": "de",
        "auth": {
            "type": "AID",
            "aid": "nasa-apps",
        }
    }

    availableProducts = {
        'long_distance_express': [1],  # ICE
        'long_distance': [2],  # IC/EC/CNL
        'regional': [8],  # RE/RB
        'suburban': [16],  # S
        'bus': [64, 128],  # BUS
        'tram': [32],  # T
        'tourismTrain': [256],  # TT
    }

    defaultProducts = [
        'long_distance_express',
        'long_distance',
        'regional',
        'suburban',
        'bus',
        'tram',
        'tourismTrain',
    ]
