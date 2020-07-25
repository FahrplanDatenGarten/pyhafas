pyHaFAS - General Information
===================================

.. image:: https://img.shields.io/pypi/v/pyhafas.svg
   :target: https://pypi.python.org/pypi/pyhafas

pyHaFAS is a client for the API of HaFAS public transport management system.

HaFAS is a software sold by the company "`HaCon <https://hacon.de/en>`_" and is used by a lot of public transport providers for routing and providing departure information to their customers.

Every public transport providers using HaFAS has their own deployment.
In general all of them use have the same API but there are some small differences between them. To cover this we have a :term:`profile` :superscript:`G` for each HaFAS deployment.

.. WARNING:: pyHaFAS is still in beta.
   The interface might change, so please read the changelog carefully before you update.

Contributing
------------
If you have a question, found a bug or want to propose a feature, have a look at `the issues page <https://github.com/n0emis/pyhafas/issues>`_.
Even better than creating an issue is creating a pull request. If you wanna do that please read the :doc:`development/guide`.


.. toctree::
   :caption: Installation and usage
   :maxdepth: 2

   usage/get_started
   usage/profiles
   usage/client
   usage/fptf
   usage/exceptions
   usage/examples

.. toctree::
   :caption: For developers

   development/guide

.. toctree::
   :caption: General

   glossary
