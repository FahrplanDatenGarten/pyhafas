import pytz

from pyhafas.profile import BaseProfile
from pyhafas.profile.gvh.helper.parse_lid import GVHParseLidHelper
from pyhafas.profile.gvh.requests.journey import GVHJourneyRequest
from pyhafas.profile.gvh.requests.journeys import GVHJourneysRequest
from pyhafas.profile.gvh.requests.station_board import GVHStationBoardRequest


class GVHProfile(BaseProfile, GVHParseLidHelper, GVHStationBoardRequest, GVHJourneysRequest, GVHJourneyRequest):
    """
    Profile of the HaFAS of Großraumverkehr Hannover (GVH) - regional in Hannover area
    """
    baseUrl = "https://gvh.hafas.de/hamm"
    defaultUserAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"

    locale = 'de-DE'
    timezone = pytz.timezone('Europe/Berlin')

    requestBody = {
        'client': {
            'id': 'HAFAS',
            'l': 'vs_webapp',
            'name': 'webapp',
            'type': 'WEB',
            'v': '10109'
        },
        'ver': '1.62',
        'lang': 'deu',
        'auth': {
            'type': 'AID',
            'aid': 'IKSEvZ1SsVdfIRSK'
        }
    }

    availableProducts = {
        "ice": [1],
        "ic-ec": [2, 4],
        "re-rb": [8],
        "s-bahn": [16],
        "stadtbahn": [256],
        "bus": [32],
        "on-demand": [512]
    }

    defaultProducts = [
        "ice",
        "ic-ec",
        "re-rb",
        "s-bahn",
        "stadtbahn",
        "bus",
        "on-demand"
    ]
