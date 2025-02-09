import datetime

from pyhafas import HafasClient
from pyhafas.profile import PKPProfile

client = HafasClient(PKPProfile())

location = '5100005' # Bydgoszcz Główna

bydgoszcz_departures = client.departures(location, date=datetime.datetime.now(), max_trips=10)
print(bydgoszcz_departures)
