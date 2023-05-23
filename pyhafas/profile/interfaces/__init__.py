from abc import ABC
from typing import Dict, List

import pytz

from pyhafas.profile.interfaces.helper.date_time import DateTimeHelperInterface
from pyhafas.profile.interfaces.helper.format_products_filter import \
    FormatProductsFilterHelperInterface
from pyhafas.profile.interfaces.helper.parse_leg import ParseLegHelperInterface
from pyhafas.profile.interfaces.helper.parse_lid import ParseLidHelperInterface
from pyhafas.profile.interfaces.helper.parse_remark import ParseRemarkHelperInterface
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
        DateTimeHelperInterface,
        ParseLegHelperInterface,
        ParseRemarkHelperInterface,
        LocationRequestInterface,
        JourneyRequestInterface,
        JourneysRequestInterface,
        StationBoardRequestInterface,
        TripRequestInterface,
        ABC):
    """
    The profile interface is the abstract class of a profile.

    It inherits all interfaces, so it has all methods a normal profile has available as abstract methods.
    Therefore it can be used as type hint for `self` in methods which are inherited by profiles.
    """
    baseUrl: str
    """Complete http(s) URL to mgate.exe of the HaFAS deployment. Other endpoints are (currently) incompatible with pyHaFAS"""
    addMicMac: bool
    """Whether the mic-mac authentication method should be activated. Exclusive with `addChecksum`"""
    addChecksum: bool
    """Whether the checksum authentication method should be activated. Exclusive with `addMicMac`"""
    salt: str
    """(required if `addMicMac` or `addChecksum` is true). The salt for calculating the checksum or mic-mac"""

    locale: str
    """(used in future) Locale used for i18n. Should be an IETF Language-Region Tag

    Examples: https://tools.ietf.org/html/bcp47#appendix-A
    """
    timezone: pytz.tzinfo.tzinfo
    """Timezone HaFAS lives in. Should be a `pytz` `timezone` object"""

    requestBody: dict
    """Static part of the request body sent to HaFAS. Normally contains informations about the client and another authentication"""

    availableProducts: Dict[str, List[int]]
    """Should contain all products available in HaFAS. The key is the name the end-user will use, the value is a list of bitmasks (numbers) needed for the product. In most cases, this is only one number. This bitmasks will be add up to generate the final bitmask."""
    defaultProducts: List[str]
    """List of products (item must be a key in `availableProducts`) which should be activated by default"""

    defaultUserAgent: str
    """(optional) User-Agent in header when connecting to HaFAS. Defaults to pyhafas. A good option would be the app ones. Can be overwritten by the user."""
    userAgent: str
    """(optional) Do not change, unless you know what you're doing. Disallows the user to change the user agent. For usage in internal code to get the user-agent which should be used."""
