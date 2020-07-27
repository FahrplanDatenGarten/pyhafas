Profile (Developer)
===================
Since every HaFAS deployment is different we have the concept of profiles for managing the differences between them.

For a "standard" HaFAS we have the :class:`BaseProfile <pyhafas.profile.base>` which contains code working for most HaFAS deployments.
This profile inherits the methods of all classes living in the folder of the profile. That classes all have an interface which defines the abstract methods of the class.

Most methods are instance methods, so they have a `self` parameter. Since the class using the method is the profile we use as type hint for `self` :class:`ProfileInterface <pyhafas.profile.interface>`.
This interface defines the variables and methods a profile has.

How to build a profile?
-----------------------
Requirements
^^^^^^^^^^^^

* You need to know how to authenticate to the HaFAS deployment. In most cases you need to know if the authentication is via mic-mac or checksum+salt and you need the salt. The salt can be get out of the source code of official apps of the transport provider or you can look if other HaFAS libraries already support the transport provider and get the salt from them
* You need the general requests body. You can get this best with mitmproxy on the offical app of the transport provider or of other libraries as in the other requirement

One good source for both requirements is `hafas-client <https://github.com/public-transport/hafas-client/tree/master/p>`_ in the specific profile folder.

Steps
^^^^^
1. Read the API of a profile. See :ref:`below <api>`.
2. Have a look on the already existing profiles and the :class:`ProfileInterface <pyhafas.profile.interface>` to get the structure of a profile.
3. Create a new product folder with a `__init__.py` file containing the profile class
4. Fill the required variables
5. Add your profile to `/pyhafas/profile/__init__.py`
6. Test if everything works
7. Yes? Perfect, add your profile in the documentation and create a pull request! No? Go on with step 8.
8. Log the request pyHaFAS sends and compare this request with the one the official app sends. Is the difference only in one specific request type or in all? If it is only in one go on stop step 8a otherwise step 8b.

  a. You could create a new class overwriting the `format`-method of the request. An example where this is done is in the VSNProfile the :func:`format_journey_request` method in the :class:`pyhafas.profile.vsn.requests.journey.VSNJourneyRequest` class.
  b. Please make sure the `requestBody` in your profile is correct. If it is, please :doc:`contact </development/introduction>` us or try to find the method causing the error yourself.

If you need help with any of that you can :doc:`contact </development/introduction>` us always!

.. _api:

API
^^^
Here are the minimum required variables of a profile (generated from :class:`ProfileInterface <pyhafas.profile.interface>`):

.. autoclass:: pyhafas.profile.interfaces.ProfileInterface
   :members:
   :undoc-members:
