import pytz

from pyhafas.profile.base.helper.date_time import BaseDateTimeHelper
from pyhafas.profile.base.helper.format_products_filter import (
    BaseFormatProductsFilterHelper,
)
from pyhafas.profile.base.helper.parse_leg import BaseParseLegHelper
from pyhafas.profile.base.helper.parse_lid import BaseParseLidHelper
from pyhafas.profile.base.helper.parse_remark import BaseParseRemarkHelper
from pyhafas.profile.base.helper.request import BaseRequestHelper
from pyhafas.profile.base.requests.journey import BaseJourneyRequest
from pyhafas.profile.base.requests.journeys import BaseJourneysRequest
from pyhafas.profile.base.requests.location import BaseLocationRequest
from pyhafas.profile.base.requests.station_board import BaseStationBoardRequest
from pyhafas.profile.base.requests.trip import BaseTripRequest
from pyhafas.profile.db.helper.request import DBRequestHelper
from pyhafas.profile.interfaces import ProfileInterface


class DBProfile(
    DBRequestHelper,
    BaseFormatProductsFilterHelper,
    BaseParseLidHelper,
    BaseDateTimeHelper,
    BaseParseLegHelper,
    BaseParseRemarkHelper,
    BaseLocationRequest,
    BaseJourneyRequest,
    BaseJourneysRequest,
    BaseStationBoardRequest,
    BaseTripRequest,
    ProfileInterface,
):
    """
    Profile of the HaFAS of Deutsche Bahn (DB) - German Railway - Regional and long-distance trains throughout Germany
    """

    addMicMac: bool = False

    baseUrl = "https://reiseauskunft.bahn.de/bin/mgate.exe"
    defaultUserAgent = "DB Navigator/19.10.04 (iPhone; iOS 13.1.2; Scale/2.00)"

    salt = "bdI8UVj40K5fvxwf"
    addChecksum = True

    locale = "de-DE"
    timezone = pytz.timezone("Europe/Berlin")

    requestBody = {
        "client": {"id": "DB", "v": "20100000", "type": "IPH", "name": "DB Navigator"},
        "ext": "DB.R21.12.a",
        "ver": "1.15",
        "auth": {"type": "AID", "aid": "n91dB8Z77MLdoR0K"},
    }

    availableProducts = {
        "long_distance_express": [1],  # ICE
        "long_distance": [2],  # IC/EC
        "regional_express": [4],  # RE/IR
        "regional": [8],  # RB
        "suburban": [16],  # S
        "bus": [32],  # BUS
        "ferry": [64],  # F
        "subway": [128],  # U
        "tram": [256],  # T
        "taxi": [512],  # Group Taxi
    }

    defaultProducts = [
        "long_distance_express",
        "long_distance",
        "regional_express",
        "regional",
        "suburban",
        "bus",
        "ferry",
        "subway",
        "tram",
        "taxi",
    ]

    def __init__(self, ua=None):
        if ua:
            self.userAgent = ua
        else:
            self.userAgent = self.defaultUserAgent
