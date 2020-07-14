from typing import Dict, List

from pyhafas.profile.base.helper.request import BaseRequestHelper
from pyhafas.profile.base.helper.format_products_filter import \
    BaseFormatProductsFilterHelper
from pyhafas.profile.base.helper.parse_lid import BaseParseLidHelper
from pyhafas.profile.base.helper.parse_date_time import BaseParseDateTimeHelper
from pyhafas.profile.base.helper.parse_leg import BaseParseLegHelper
from pyhafas.profile.base.requests.location import BaseLocationRequest
from pyhafas.profile.base.requests.journey import BaseJourneyRequest
from pyhafas.profile.base.requests.journeys import BaseJourneysRequest
from pyhafas.profile.base.requests.station_board import BaseStationBoardRequest
from pyhafas.profile.base.requests.trip import BaseTripRequest
from pyhafas.profile.interfaces import ProfileInterface


class BaseProfile(
        BaseRequestHelper,
        BaseFormatProductsFilterHelper,
        BaseParseLidHelper,
        BaseParseDateTimeHelper,
        BaseParseLegHelper,
        BaseLocationRequest,
        BaseJourneyRequest,
        BaseJourneysRequest,
        BaseStationBoardRequest,
        BaseTripRequest,
        ProfileInterface):
    baseUrl: str = ""
    defaultUserAgent: str = 'pyhafas'

    addMicMac: bool = False
    addChecksum: bool = False
    salt: str = ""

    locale: str = 'de-DE'
    timezone: str = 'Europe/Berlin'

    requestBody: dict = {}

    available_products: Dict[str, List[int]] = {}
    default_products: List[str] = []

    def __init__(self, ua=defaultUserAgent):
        self.userAgent = ua
