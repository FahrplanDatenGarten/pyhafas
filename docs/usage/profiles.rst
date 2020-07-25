Profiles
========
Here's a list of all HaFAS deployments pyHaFAS supports. If the :term:`profile` :superscript:`G` has any differences, they will be mentioned here.

Deutsche Bahn (DB)
------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import DBProfile
  client = HafasClient(DBProfile())

Verkehrsverbund Süd-Niedersachsen (VSN)
---------------------------------------
Usage
^^^^^^
.. code:: python

  from pyhafas.profile import VSNProfile
  client = HafasClient(VSNProfile())
