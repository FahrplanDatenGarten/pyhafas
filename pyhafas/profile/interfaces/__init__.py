from abc import ABC
from typing import Dict, List

from pyhafas.profile.interfaces.helper.format_products_filter import \
    FormatProductsFilterHelperInterface
from pyhafas.profile.interfaces.helper.parse_date_time import \
    ParseDateTimeHelperInterface
from pyhafas.profile.interfaces.helper.parse_leg import ParseLegHelperInterface
from pyhafas.profile.interfaces.helper.parse_lid import ParseLidHelperInterface
from pyhafas.profile.interfaces.helper.request import RequestHelperInterface
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.profile.interfaces.requests.journeys import \
    JourneysRequestInterface
from pyhafas.profile.interfaces.requests.location import \
    LocationRequestInterface
from pyhafas.profile.interfaces.requests.station_board import \
    StationBoardRequestInterface
from pyhafas.profile.interfaces.requests.trip import TripRequestInterface


class ProfileInterface(
        RequestHelperInterface,
        FormatProductsFilterHelperInterface,
        ParseLidHelperInterface,
        ParseDateTimeHelperInterface,
        ParseLegHelperInterface,
        LocationRequestInterface,
        JourneyRequestInterface,
        JourneysRequestInterface,
        StationBoardRequestInterface,
        TripRequestInterface,
        ABC):
    baseUrl: str
    defaultUserAgent: str
    userAgent: str

    addMicMac: bool
    addChecksum: bool
    salt: str

    locale: str
    timezone: str

    requestBody: dict

    available_products: Dict[str, List[int]]
    default_products: List[str]
