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
