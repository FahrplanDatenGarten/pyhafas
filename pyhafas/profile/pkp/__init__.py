import pytz

from pyhafas.profile import BaseProfile
from pyhafas.profile.pkp.requests.journeys import PKPJourneysRequest
from pyhafas.profile.pkp.requests.journey import PKPJourneyRequest


class PKPProfile(PKPJourneysRequest, PKPJourneyRequest, BaseProfile):
    """
    Profile of the HaFAS of Polskie Koleje Państwowe (PKP) – Polish State Railways 
    """
    baseUrl = "https://mobil.rozklad-pkp.pl:8019/bin/mgate.exe"
    defaultUserAgent = 'Dalvik/3.1.0' # Must be set to that value.

    locale = 'pl-PL'
    timezone = pytz.timezone('Europe/Warsaw')

    requestBody = {
        'client': {
            'type': 'AND',
            'id': 'HAFAS'
        },
        'ext': 'DB.R21.12.a',
        'ver': '1.58',
        'lang': 'deu',
        'auth': {
            'type': 'AID',
            'aid': 'DrxJYtYZQpEBCtcb'
        }
    }

    availableProducts = {
        'high-speed-train': [1, 2],
        'long-distance-train': [4],
        'regional-train': [8],
        'bus': [32],
    }

    defaultProducts = [
        'high-speed-train',
        'long-distance-train',
        'regional-train',
        'bus'
    ]
