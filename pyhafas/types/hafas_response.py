import json

import requests

from pyhafas.profile.interfaces.mappings.error_codes import ErrorCodesMappingInterface


class HafasResponse:
    def __init__(self, raw_hafas_response: requests.Response, mapping: ErrorCodesMappingInterface):
        data = json.loads(raw_hafas_response.text)
        self.check_for_errors(data, mapping)
        self.common = data['svcResL'][0]['res']['common']
        self.res = data['svcResL'][0]['res']

    def check_for_errors(self, data: dict, mapping: ErrorCodesMappingInterface):
        error_not_found = False
        if data.get('err', "OK") != "OK":
            try:
                raise mapping[data['err']].value(data.get('errTxt', ''))
            except KeyError:
                error_not_found = True

        if error_not_found:
            raise mapping['default'].value(data.get('errTxt', ''))

        if not data.get('svcResL', False):
            raise mapping['default'].value("HaFAS response cannot be parsed")

        if data['svcResL'][0].get('err', "OK") != "OK":
            try:
                raise mapping[data['svcResL'][0]['err']].value(data['svcResL'][0].get('errTxt', ''))
            except KeyError:
                error_not_found = True

        if error_not_found:
            raise mapping['default'].value(data['svcResL'][0].get('errTxt', ''))
