import datetime

from pyhafas import HafasClient
from pyhafas.profile import RKRPProfile

client = HafasClient(RKRPProfile(), debug=True)

id_nordhavn='8600653'
id_kongebakken9='A=2@O=Kongebakken 9, 2765 Smørum, Egedal Kommune@X=12294403@Y=55749256@U=103@L=902400113@B=1@p=1618386996@'

#print(client.departures(
#    station=id_nordhavn,
#    date=datetime.datetime.now(),
#    max_trips=5
#))

#print(client.arrivals(
#    station=id_nordhavn,
#    date=datetime.datetime.now(),
#    max_trips=5
#))

# Test searching for an address
locs = client.locations("Kongebakken 9, 2765 Smørum", rtype='ALL')
assert(locs[0].lid == id_kongebakken9)


possibilities = client.journeys(
    origin          = id_nordhavn,
    destination     = id_kongebakken9,
    date            = datetime.datetime.now(),
    min_change_time = 0,
    max_changes     = -1
)


for p in possibilities:
    print('--------')
    for l in p.legs:
        print(l.departure, l.origin.name, "--> " + str(l.name) + " -->" )

    l = p.legs[-1]
    print(l.arrival, l.destination.name)
    print("Journey duration: ", p.duration)
