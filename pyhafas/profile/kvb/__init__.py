import pytz

from pyhafas.profile import BaseProfile
from pyhafas.profile.kvb.requests.journeys import KVBJourneysRequest
from pyhafas.profile.kvb.requests.journey import KVBJourneyRequest


class KVBProfile(KVBJourneysRequest, KVBJourneyRequest, BaseProfile):
    """
    Profile of the HaFAS of Kölner Verkehrsbetriebe (KVB) - Regional in Cologne
    """
    baseUrl = "https://auskunft.kvb.koeln/gate"

    locale = 'de-DE'
    timezone = pytz.timezone('Europe/Berlin')

    requestBody = {
        'client': {
            'id': 'HAFAS',
            'l': 'vs_webapp',
            'v': '154',
            'type': 'WEB',
            'name': 'webapp'
        },
        'ext': 'DB.R21.12.a',
        'ver': '1.58',
        'lang': 'deu',
        'auth': {
            'type': 'AID',
            'aid': 'Rt6foY5zcTTRXMQs'
        }
    }

    availableProducts = {
        's-bahn': [1],
        'stadtbahn': [2],
        'bus': [8],
        'fernverkehr': [32],
        'regionalverkehr': [64],
        'taxibus': [256]
    }

    defaultProducts = [
        's-bahn',
        'stadtbahn',
        'bus',
        'fernverkehr',
        'regionalverkehr',
        'taxibus',
    ]
