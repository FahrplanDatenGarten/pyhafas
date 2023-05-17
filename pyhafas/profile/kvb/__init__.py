import pytz

from pyhafas.profile import BaseProfile


class KVBProfile(BaseProfile):
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
        'suburban': [1],  # S
        'tram': [2],  # U
        'bus': [8],  # BUS
        'long_distance': [32],  # ICE/IC/EC
        'regional': [46],  # RE/IR/RB
        'taxibus': [256]  # taxi bus
    }

    defaultProducts = [
        'suburban',
        'tram',
        'bus',
        'long_distance',
        'regional',
        'taxibus'
    ]
