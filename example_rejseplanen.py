import datetime

from pyhafas import HafasClient
from pyhafas.profile import RKRPProfile

client = HafasClient(RKRPProfile(), debug=True)

# Human input strings
id_nordhavn = 'Nordhavn St.'
id_kongebakken9 = 'Kongebakken 9, 2765 Smørum'

# Resolve human string into Location-ID
lids_kongebakken9 = client.locations(id_kongebakken9, rtype='ALL')
lid_kongebakken9 = lids_kongebakken9[0].lid  # First is good-enough
assert('Kongebakken 9, 2765 Smørum, Egedal Kommune' in lid_kongebakken9)

lids_nordhavn = client.locations(id_nordhavn, rtype='ALL')
lid_nordhavn = lids_nordhavn[0].lid  # First is good-enough
assert('Nordhavn St' in lid_nordhavn)

#print(client.departures(
#    station=lid_nordhavn,
#    date=datetime.datetime.now(),
#    max_trips=5
#))

#print(client.arrivals(
#    station=lid_nordhavn,
#    date=datetime.datetime.now(),
#    max_trips=5
#))

possibilities = client.journeys(
    origin          = lid_nordhavn,
    destination     = lid_kongebakken9,
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
