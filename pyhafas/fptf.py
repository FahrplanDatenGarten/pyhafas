class Station:
    def __init__(self, id: str or int, **kwargs):
        self.id = id
        self.name: str = kwargs.get('name')

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class Journey:
    def __init__(self, id: str or int):
        self.id = id

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

class Leg:
    def __init__(self, **kwargs):
        origin: Station = kwargs.get('origin')
        destination: Station = kwargs.get('destination')

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)