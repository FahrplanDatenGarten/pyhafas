import base64
import codecs
import datetime
import json
import re
from hashlib import md5
from typing import List

import requests
from Crypto.Cipher import AES

from .journey import Journey
from .profile import Profile


class HafasClient:
    def __init__(
            self,
            debug: bool = False,
            base_url: str = None,
            profile: Profile = None):
        pass

    def departures(self, station):
        pass

    def arrivals(self, station):
        pass

    def journeys(self, origin, destination) -> List[Journey]:
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
