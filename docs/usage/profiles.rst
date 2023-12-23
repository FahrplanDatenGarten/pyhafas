Profiles
========
Here's a list of all HaFAS deployments pyHaFAS supports.
If the :term:`profile`:superscript:`G` has any differences, they will be mentioned here. Also, available and default :term:`products <product>`:superscript:`G` are defined.

Deutsche Bahn (DB)
------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import DBProfile
  client = HafasClient(DBProfile())

Available Products
^^^^^^^^^^^^^^^^^^

===================== ==================
pyHaFAS Internal Name Example Train Type
===================== ==================
long_distance_express ICE/ECE
long_distance         IC/EC
regional_express      RE/IRE
regional              RB
suburban              S
bus                   BUS
ferry                 F
subway                U
tram                  STR/T
taxi                  Group Taxi
===================== ==================

Default Products
^^^^^^^^^^^^^^^^
All available products specified above are enabled by default.

Other interesting Stuff
^^^^^^^^^^^^^^^^^^^^^^^
* Mapping list with station IDs exists: `<https://data.deutschebahn.com/dataset/data-haltestellen>`_

Verkehrsverbund Süd-Niedersachsen (VSN)
---------------------------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import VSNProfile
  client = HafasClient(VSNProfile())

Available Products
^^^^^^^^^^^^^^^^^^

===================== ==================
pyHaFAS Internal Name Example Train Type
===================== ==================
long_distance_express ICE/ECE
long_distance         IC/EC/CNL
regional_express      RE/IRE
regional              NV (e.g. RB)
suburban              S
bus                   BUS
ferry                 F
subway                U
tram                  STR/T
anruf_sammel_taxi     Group Taxi
===================== ==================

Default Products
^^^^^^^^^^^^^^^^
All available products specified above are enabled by default.

Specialities
^^^^^^^^^^^^

* The `max_trips` filter in station board (departures/arrival) requests seems not to work


Nahverkehr Sachsen-Anhalt (NASA)
---------------------------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import NASAProfile
  client = HafasClient(NASAProfile())

Available Products
^^^^^^^^^^^^^^^^^^

===================== ==================
pyHaFAS Internal Name Example Train Type
===================== ==================
long_distance_express ICE/ECE
long_distance         IC/EC/CNL
regional              RE / RB
suburban              S
bus                   BUS
tram                  STR/T
tourism_train         TT
===================== ==================

Default Products
^^^^^^^^^^^^^^^^
All available products specified above are enabled by default.

Specialities
^^^^^^^^^^^^

Part of NASA are tourism trains, for example the 'Harzer Schmalspurbahnen' (Light railway of Harz) which climbs the Brocken mountain (1141m).



Kölner Verkehrsbetriebe (KVB)
-----------------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import KVBProfile
  client = HafasClient(KVBProfile())

Available Products
^^^^^^^^^^^^^^^^^^

===================== ==================
pyHaFAS Internal Name Example Train Type
===================== ==================
s-bahn                S
stadtbahn             U
bus                   BUS
fernverkehr           ICE/ECE/IC/EC
regionalverkehr       RE/IRE
taxibus               Group Taxi
===================== ==================

Default Products
^^^^^^^^^^^^^^^^
All available products specified above are enabled by default.


Verkehrsverbund Vorarlberg (VVV)
-----------------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import VVVProfile
  client = HafasClient(VVVProfile())

Available Products
^^^^^^^^^^^^^^^^^^

===================== ==================
pyHaFAS Internal Name Train Type
===================== ==================
train-and-s-bahn      Bahn & S-Bahn
u-bahn                U-Bahn
tram                  Straßenbahn
long-distance-bus     Fernbus
regional-bus          Regionalbus
city-bus              Stadtbus
aerial-lift           Seil-/Zahnradbahn
ferry                 Schiff
on-call               Anrufsammeltaxi
other-bus             sonstige Busse
===================== ==================

Default Products
^^^^^^^^^^^^^^^^
All available products specified above are enabled by default.