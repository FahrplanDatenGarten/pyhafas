import base64
import codecs
import datetime
import json
import re
from hashlib import md5

import requests
from Crypto.Cipher import AES

from .profiles import Profile


class HafasClient:
    def __init__(self, debug: Bool=false, base_url: str=None, profile: Profile):
        pass

    def departures(self, station):
        pass

    def arrivals(self, station):
        pass

    def journeys(self, from, to) -> List[Journey]:
        pass

    def locations(self, term):
        pass

    def stop(self, stop):
        pass

    def nearby(self, location):
        pass

    def trip(self, id, name):
        pass

    def radar(self):  # What is this for?
        pass
