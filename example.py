import datetime

from pyhafas import HafasClient
from pyhafas.profile import DBProfile, VSNProfile

client = HafasClient(DBProfile(), debug=True)

# print(client.departures('8000128'))

# print(client.arrivals('8000128'))
# print(client.journey('¶HKI¶T$A=1@O=Berlin Jungfernheide@L=8011167@a=128@$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$202002101544$202002101549$RB 18521$$1$§T$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$A=1@O=München Hbf@L=8000261@a=128@$202002101605$202002102002$ICE 1007$$1$'))
print(
    client.journeys(
        destination=8000128,
        origin=8005556,
        via=[
            8070003
        ],
        date=datetime.datetime(
            year=2020,
            month=5,
            day=31,
            hour=20,
            minute=44,
            second=00),
        min_change_time=2,
        max_changes=1
    )
)
# print(client.location("Köln Hbf"))

print('='*20)
vsn = HafasClient(VSNProfile())
print(vsn.departures('9034033'))
