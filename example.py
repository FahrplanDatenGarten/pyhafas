from pyhafas import HafasClient
from pyhafas.profile import DBProfile

client = HafasClient(DBProfile(), debug=True)

dep = client.departures('8000128')

# print(client.arrivals('8000128'))
# print(client.journey('¶HKI¶T$A=1@O=Berlin Jungfernheide@L=8011167@a=128@$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$202002101544$202002101549$RB 18521$$1$§T$A=1@O=Berlin Hbf (tief)@L=8098160@a=128@$A=1@O=München Hbf@L=8000261@a=128@$202002101605$202002102002$ICE 1007$$1$'))
# print(client.journeys('008000128', '008100113'))
# print(client.location("Köln Hbf"))

print(dep)