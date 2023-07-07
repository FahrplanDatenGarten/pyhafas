Changelog
=========

.. contents::

v0.4.0
------
* [feature] Parse leg remarks
* [feature] Add KVB Profile
* [feature] Add optional retry parameter for requests. You might activate retries with the `activate_retry()` function on your profile

v0.3.1
------
* [BUG] Fix setting of default user agent

v0.3.0
------
* [FEATURE] Add timezone awareness to all datetime time objects
* [FEATURE] Allow filtering at :func:`pyhafas.client.HafasClient.departures` and :func:`pyhafas.client.HafasClient.arrivals` for direction station
* [FEATURE] Add option to :func:`pyhafas.client.HafasClient.journeys` request to allow setting a maximum number of returned journeys
* [BUG] Fix bug with some HaFAS versions in platform parsing
* [BUG] Changed coordinate type from int to float
* Better dependency requirements (less specific versions)
* Add tests

v0.2.0
------
* [BREAKING] Changed return format of :func:`pyhafas.client.HafasClient.arrivals` and :func:`pyhafas.client.HafasClient.departures` methods
* [BREAKING] Removed deprecated parameter `max_journeys` in :func:`pyhafas.client.HafasClient.arrivals` and :func:`pyhafas.client.HafasClient.departures` methods
* [BUG] Fixed :func:`pyhafas.client.HafasClient.journey` request in VSN-Profile
