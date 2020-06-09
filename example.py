import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile, VSNProfile

client = HafasClient(DBProfile(), debug=True)

print(client.departures(
    station='8000128',
    date=datetime.datetime.now(),
    max_journeys=5
))

print(client.arrivals(
    station='8005556',
    date=datetime.datetime.now(),
    max_journeys=5
))
print(client.journey('¶HKI¶T$A=1@O=Berlin Jungfernheide@L=8011167@a=128@$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$202002101544$202002101549$RB 18521$$1$§T$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$A=1@O=München Hbf@L=8000261@a=128@$202002101605$202002102002$ICE 1007$$1$'))
print(client.journeys(
        destination=8000207,
        origin=8005556,
        date=datetime.datetime.now(),
        min_change_time=0,
        max_changes=-1
    ))
print(client.locations("Köln Hbf"))

print(client.trip("1|1372374|3|80|9062020"))

print('='*20)
vsn = HafasClient(VSNProfile())
print(vsn.departures(
    station='9034033',
    date=datetime.datetime.now(),
    max_journeys=5
))
