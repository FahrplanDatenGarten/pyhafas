from pyhafas.profile.interfaces.mappings.error_codes import \
    ErrorCodesMappingInterface
from pyhafas.types.exceptions import (AccessDeniedError, AuthenticationError,
                                      GeneralHafasError,
                                      JourneysArrivalDepartureTooNearError,
                                      JourneysTooManyTrainsError,
                                      LocationNotFoundError,
                                      TripDataNotFoundError)


class BaseErrorCodesMapping(ErrorCodesMappingInterface):
    default = GeneralHafasError
    AUTH = AuthenticationError
    R5000 = AccessDeniedError
    LOCATION = LocationNotFoundError
    H500 = JourneysTooManyTrainsError
    H890 = JourneysArrivalDepartureTooNearError
    SQ005 = TripDataNotFoundError
    TI001 = TripDataNotFoundError
