import json

import requests

from pyhafas.profile.interfaces.mappings.error_codes import \
    ErrorCodesMappingInterface


class HafasResponse:
    def __init__(self, raw_hafas_response: requests.Response,
                 mapping: ErrorCodesMappingInterface):
        data = json.loads(raw_hafas_response.text)
        self.raw_hafas_response = raw_hafas_response
        self.data = data
        self.check_for_errors(mapping)

    def check_for_errors(self, mapping: ErrorCodesMappingInterface):
        error_not_found = False
        if self.data.get('err', "OK") != "OK":
            try:
                raise mapping[self.data['err']].value(self.data.get('errTxt', ''))
            except KeyError:
                error_not_found = True
        if error_not_found:
            raise mapping['default'].value(self.data.get('errTxt', ''))

        if not self.data.get('svcResL', False):
            raise mapping['default'].value("HaFAS response cannot be parsed")

        if self.data['svcResL'][0].get('err', "OK") != "OK":
            try:
                raise mapping[self.data['svcResL'][0]['err']].value(
                    self.data['svcResL'][0].get('errTxt', ''))
            except KeyError:
                error_not_found = True
        if error_not_found:
            raise mapping['default'].value(self.data['svcResL'][0].get('errTxt', ''))

    @property
    def common(self):
        return self.data['svcResL'][0]['res']['common']

    @property
    def res(self):
        return self.data['svcResL'][0]['res']
