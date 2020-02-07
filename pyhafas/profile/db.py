from . import Profile


class DBProfile(Profile):
    baseUrl = "https://reiseauskunft.bahn.de/bin/mgate.exe"

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

    def __init__(self):
        pass
