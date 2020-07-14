from pyhafas.profile.base import BaseProfile


class DBProfile(BaseProfile):
    baseUrl = "https://reiseauskunft.bahn.de/bin/mgate.exe"
    defaultUserAgent = "DB Navigator/19.10.04 (iPhone; iOS 13.1.2; Scale/2.00)"

    salt = 'bdI8UVj40K5fvxwf'
    addChecksum = True

    locale = 'de-DE'
    timezone = 'Europe/Berlin'

    requestBody = {
        'client': {
            'id': 'DB',
            'v': '16040000',
            'type': 'IPH',
            'name': 'DB Navigator'
        },
        'ext': 'DB.R19.04.a',
        'ver': '1.16',
        'auth': {
            'type': 'AID',
            'aid': 'n91dB8Z77MLdoR0K'
        }
    }

    available_products = {
        'long_distance_express': [1],  # ICE
        'long_distance': [2],  # IC/EC
        'regional_express': [4],  # RE/IR
        'regional': [8],  # RB
        'suburban': [16],  # S
        'bus': [32],  # BUS
        'ferry': [64],  # F
        'subway': [128],  # U
        'tram': [256],  # T
        'taxi': [512]  # Group Taxi
    }

    default_products = [
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
