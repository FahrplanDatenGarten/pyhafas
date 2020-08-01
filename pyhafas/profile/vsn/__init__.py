from pyhafas.profile import BaseProfile
from pyhafas.profile.vsn.requests.journey import VSNJourneyRequest


class VSNProfile(VSNJourneyRequest, BaseProfile):
    """
    Profile for the HaFAS of "Verkehrsverbund Süd-Niedersachsen" (VSN) - local transportation provider
    """
    baseUrl = "https://fahrplaner.vsninfo.de/hafas/mgate.exe"
    defaultUserAgent = "vsn/5.3.1 (iPad; iOS 13.3; Scale/2.00)"

    salt = 'SP31mBufSyCLmNxp'
    addMicMac = True

    locale = 'de-DE'
    timezone = 'Europe/Berlin'

    requestBody = {
        'client': {
            'id': 'VSN',
            'v': '5030100',
            'type': 'IPA',
            'name': 'vsn',
            'os': 'iOS 13.3'
        },
        'ver': '1.24',
        'lang': 'de',
        'auth': {
            'type': 'AID',
            'aid': 'Mpf5UPC0DmzV8jkg'
        }
    }

    availableProducts = {
        'long_distance_express': [1],  # ICE
        'long_distance': [2],  # IC/EC/CNL
        'regional_express': [4],  # RE/IR
        'regional': [8],  # NV
        'suburban': [16],  # S
        'bus': [32],  # BUS
        'ferry': [64],  # F
        'subway': [128],  # U
        'tram': [256],  # T
        'anruf_sammel_taxi': [512]  # Group Taxi
    }

    defaultProducts = [
        'long_distance_express',
        'long_distance',
        'regional_express',
        'regional',
        'suburban',
        'bus',
        'ferry',
        'subway',
        'tram',
        'anruf_sammel_taxi'
    ]
