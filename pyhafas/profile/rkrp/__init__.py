import pytz

from pyhafas.profile.base import BaseProfile


class RKRPProfile(BaseProfile):
    """
    Profile of the HaFAS of Rejsekort & Rejseplan (RKRP) - Danish {Railway, Bus, Metro, etc.}.
    https://www.rejsekort.dk/da/RKRP
    https://help.rejseplanen.dk/hc/da/articles/214174465-Rejseplanens-API
    """

    # Alternative base URLs (mostly CNAMEs):
    #     rejseplanen.dk
    #     webapp.rejseplanen.dk
    #     www.rejseplanen.dk
    #     rkrp.hafas.cloud
    #     rkrp-fat.hafas.cloud
    baseUrl = "https://www.rejseplanen.dk/bin/iphone.exe"
    defaultUserAgent = "Dalvik/2.1.0 (Linux; U; Android 11; Pixel 4a Build/RQ2A.210305.006)"

    addMicMac = False
    addChecksum = False

    locale = 'da-DK'
    timezone = pytz.timezone('Europe/Copenhagen')

    requestBody = {
        "client": {
            "id": "DK",
            "type": "WEB",
            "name": "rejseplanwebapp",
            "l": "vs_webapp"
        },
        "ext": "DK.11",
        "ver": "1.24",
        "lang": "dan",
        "auth": {
            "type": "AID",
            "aid": "j1sa92pcj72ksh0-web"
        }
    }

    availableProducts = {
        'long_distance_express': [1],  # ICE
        'long_distance': [2],  # IC/EC
        'regional_express': [4],  # RE/IR
        'regional': [8],  # RB
        'suburban': [16],  # S
        'bus': [32],  # BUS
        'ferry': [64],  # F
        'subway': [128],  # U
        'tram': [256, 2048],  # T
        'taxi': [512]  # Group Taxi
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
        'taxi'
    ]
