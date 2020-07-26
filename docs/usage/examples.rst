Usage Examples
==============
Below you can find usage examples for each method available in :doc:`HafasClient </usage/client>`.

General Information
-------------------
In the following code blocks we only use :func:`departures <pyhafas.client.HafasClient.departures>` but not :func:`arrivals <pyhafas.client.HafasClient.arrivals>`.
Those methods are pretty same, so every time we use :func:`departures <pyhafas.client.HafasClient.departures>` you can exchange this with :func:`arrivals <pyhafas.client.HafasClient.arrivals>`.

We also only use some of the supported clients. The client can be exchanged, if not specified otherwise.

.. _example1:

1. locations + departures
-------------------------

The below code gets the departing long distance trains at the station with the best similarity when searching for "Siegburg/Bonn".
Let's get to the parts of the code:

1. The required classes are imported, a :class:`HafasClient <pyhafas.client.HafasClient>` is created with the :class:`DBProfile <pyhafas.profile.DBProfile>`
2. **Location-Search**

  1. The :class:`HafasClient <pyhafas.client.HafasClient>` searches for locations with the term "Siegburg/Bonn".
  2. The best location is chosen from the list (first object in the list is that with highest similarity)

3. The :class:`HafasClient <pyhafas.client.HafasClient>` searches for maximum 2 trips with the following criteria:

  * departing now
  * at the best location (from step 2)
  * with the products in the categories `long_distance_express` or `long_distance`. `long_distance` is enabled per default and so per default in the list of enabled products and all others (except `long_distance_express`) are disabled.

*long_distance_express is also enabled per default but it can be in the list with True as value to guarantee it's enabled, if it wouldn't be enabled by default, it would be enabled now*

.. code:: python

  import datetime
  from typing import List

  # Part 1
  from pyhafas import HafasClient
  from pyhafas.profile import DBProfile
  from pyhafas.types.fptf import Leg

  client = HafasClient(DBProfile())

  # Part 2
  locations = client.locations("Siegburg/Bonn")
  best_found_location = locations[0]
  print(best_found_location)  # <class 'pyhafas.types.fptf.Station'>({'id': '008005556', 'name': 'Siegburg/Bonn', 'latitude': 50.794051, 'longitude': 7.202616})

  # Part 3
  departures: List[Leg] = client.departures(
      station=best_found_location.id,
      date=datetime.datetime.now(),
      max_trips=2,
      products={
          'long_distance_express': True,
          'regional_express': False,
          'regional': False,
          'suburban': False,
          'bus': False,
          'ferry': False,
          'subway': False,
          'tram': False,
          'taxi': False
      }
  )
  print(departures)  # [<class 'pyhafas.types.fptf.Leg'>({...}), <class 'pyhafas.types.fptf.Leg'>({...})]

.. _example2:

2. departures + trip
--------------------
The below code get the next departing trip at the station "Siegburg/Bonn" (with the id `008005556`) and gets after that detailed information with the :func:`trip <pyhafas.client.HafasClient.trip>` method.

Currently the :func:`trip <pyhafas.client.HafasClient.trip>` method gives the same data as :func:`departures <pyhafas.client.HafasClient.departures>`, but in future versions there will be more data available in :func:`trip <pyhafas.client.HafasClient.trip>`.

Using the :func:`trip <pyhafas.client.HafasClient.trip>` method is also useful to refresh the data about a specific trip by its ID.

.. code:: python

  import datetime

  # Part 1
  from pyhafas import HafasClient
  from pyhafas.profile import DBProfile
  from pyhafas.types.fptf import Leg

  client = HafasClient(DBProfile())

  # Part 2
  departure: Leg = client.departures(
      station="008005556",
      date=datetime.datetime.now(),
      max_trips=1
  )[0]
  print(departure)  # <class 'pyhafas.types.fptf.Leg'>({'id': '1|236759|0|80|26072020', ...})

  # Part 3
  trip: Leg = client.trip(departure.id)
  print(trip)  # <class 'pyhafas.types.fptf.Leg'>({'id': '1|236759|0|80|26072020', ...})

.. _example3:

3. locations + journeys + journey
---------------------------------
In the code block below we create search for possible journeys between the stations "Göttingen Bahnhof/ZOB" and "Góttingen Campus" via "Göttingen Angerstraße".

For explanation of the first and second part please look at :ref:`example 1 <example1>`. After the code there is also a visualization of a journey HaFAS returns for this request.

In part 3 the HafasClient searches for journeys with the following criteria:

* origin station is "Göttingen Bahnhof/ZOB"
* destination station is "Göttingen Campus"
* the journey must be via "Göttingen Angerstraße"
* the journey may have a maximum of 1 transfer
* each transfer must have at least a time of 15 minutes

In part 4 the journey data of of the first journey found in part 3 is refreshed.

.. code:: python

  import datetime

  # Part 1
  from pyhafas import HafasClient
  from pyhafas.profile import VSNProfile
  from pyhafas.types.fptf import Leg

  client = HafasClient(VSNProfile())

  # Part 2
  location_goe_bf = client.locations("Göttingen Bahnhof/ZOB")[0]
  location_goe_ang = client.locations("Göttingen Angerstraße")[0]
  location_goe_campus = client.locations("Göttingen Campus")[0]

  # Part 3
  journeys = client.journeys(
      origin=location_goe_bf,
      via=[location_goe_ang],
      destination=location_goe_campus,
      date=datetime.datetime.now(),
      max_changes=1,
      min_change_time=15
  )
  print(journeys)  # [<class 'pyhafas.types.fptf.Journey'>({...}), <class 'pyhafas.types.fptf.Journey'>({...}), <class 'pyhafas.types.fptf.Journey'>({...}), ...]})]

  # Part 4
  journey = client.journey(journeys[0].id)

  print(journey)  # <class 'pyhafas.types.fptf.Journey'>({...})

*As short form for Göttingen we use GOE*

Here is a table with the journey in the variable `journey` of the code example above.
Here some explanation on the routing algorithm of HaFAS:

* You might see that the walk leg is exactly 15 minutes. This is because we set a minimum change time of 15 minutes. A normal walking time would be about 5 minutes.
* A walk leg does not count in the number of changes between legs. The maximum number of changes only specifies between how much vehicles you change.
* You might think that there's a bug because the via station (GOE Angerstraße, 2) is not in the table below. That's correct. For HaFAS it's enough when a vehicle stops at the via station. In this example the first and second bus both stops at "GOE Angerstraße".

===================== ===================== ============== ============ =================
origin station        destination station   departure time arrival time mode of transport
===================== ===================== ============== ============ =================
GOE Bahnhof (1)       GOE Neues Rathaus (3) 11:40          11:44        BUS
GOE Neues Rathaus (3) GOE Bürgerstraße (4)  11:44          11:59        WALKING
GOE Bürgerstraße (4)  GOE Campus (5)        12:00          12:13        BUS
===================== ===================== ============== ============ =================

.. figure:: /_static/usage/images/examples_3_journeys_map.jpg

.. centered:: map showing the stations, © OpenStreetMap contributors. Tiles courtesy of MeMoMaps.


