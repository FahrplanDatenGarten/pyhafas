Get started
===========

Terminology
-----------
In pyHaFAS we often use the followings terms. Please read them, so you can understand the documentation and project better.

Most other pyHaFAS-specific words are defined in the :doc:`/glossary`.
If one of this words is used in this documentation it's marked as a link with a superscript G as follows: :term:`profile`:superscript:`G`


======= =======
Term    Meaning
======= =======
profile Customization for each HaFAS deployment - Contains the endpoint, tokens and possible changes for the deployment
FPTF    Abbreviation for `Friendly Public Transport Format <https://github.com/public-transport/friendly-public-transport-format/blob/master/spec/readme.md>`_ - Used as basis for returned data
======= =======

Installation
------------
You only need to install the pyhafas package, for example using pip:

.. code:: console

    $ pip install pyhafas

Sample Starter Code
-------------------
Below is a sample code for an easy usage. It has multiple parts:

1. It imports the :class:`HafasClient <pyhafas.client.HafasClient>` and the :class:`DBProfile <pyhafas.profile.db.DBProfile>` of pyHaFAS and creates the :class:`HafasClient <pyhafas.client.HafasClient>` with the :term:`profile`:superscript:`G`. The :class:`DBProfile <pyhafas.profile.db.DBProfile>` is the :term:`profile`:superscript:`G` belonging to the HaFAS deployment of Deutsche Bahn.

2. It searches for locations (stations) with the term "Berlin" and prints the result

3. It searches for departing trains at Berlin Central Station. Every station is identified by an ID, which (in this case `8011160`) can be obtained by a `location`-request with pyhafas.

.. code:: python

  from pyhafas import HafasClient
  from pyhafas.profile import DBProfile

  client = HafasClient(DBProfile())

  print(client.locations("Berlin"))

  print(client.departures(
      station='8011160',
      date=datetime.datetime.now(),
      max_journeys=5
  ))

What's next?
------------

For a good start with pyHaFAS you should go on reading the documentation. Especially the pages :doc:`/usage/examples` and :doc:`profiles` are a good start.
