import json


class PyTestHafasResponse:
    def __init__(self, raw_hafas_response: str):
        self.raw_hafas_response = raw_hafas_response
        data = json.loads(raw_hafas_response)
        self.data = data

    @property
    def common(self):
        return self.data['svcResL'][0]['res']['common']

    @property
    def res(self):
        return self.data['svcResL'][0]['res']
