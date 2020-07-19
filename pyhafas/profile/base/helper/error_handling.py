from pyhafas.exceptions import GeneralHafasError, AuthenticationError, AccessDeniedError, LocationNotFoundError, \
    JourneysTooManyTrainsError, JourneysArrivalDepartureTooNearError, TripDataNotFoundError
from pyhafas.profile import ProfileInterface
from pyhafas.profile.interfaces.helper.error_handling import ErrorHandlingHelperInterface, ErrorCodesMappingInterface


class BaseErrorCodesMapping(ErrorCodesMappingInterface):
    default = GeneralHafasError
    AUTH = AuthenticationError
    R5000 = AccessDeniedError
    LOCATION = LocationNotFoundError
    H500 = JourneysTooManyTrainsError
    H890 = JourneysArrivalDepartureTooNearError
    SQ005 = TripDataNotFoundError
    TI001 = TripDataNotFoundError


class BaseErrorHandlingHelper(ErrorHandlingHelperInterface):
    def check_for_errors(self: ProfileInterface, data: dict):
        error_not_found = False
        if data.get('err', "OK") != "OK":
            try:
                raise BaseErrorCodesMapping[data['err']].value(data.get('errTxt', ''))
            except KeyError:
                error_not_found = True

        if error_not_found:
            raise BaseErrorCodesMapping['default'].value(data.get('errTxt', ''))

        if not data.get('svcResL', False):
            raise BaseErrorCodesMapping['default'].value("HaFAS response cannot be parsed")

        if data['svcResL'][0].get('err', "OK") != "OK":
            try:
                raise BaseErrorCodesMapping[data['svcResL'][0]['err']].value(data['svcResL'][0].get('errTxt', ''))
            except KeyError:
                error_not_found = True

        if error_not_found:
            raise BaseErrorCodesMapping['default'].value(data['svcResL'][0].get('errTxt', ''))
