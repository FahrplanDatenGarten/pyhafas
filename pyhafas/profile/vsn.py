from . import Profile


class VSNProfile(Profile):
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
