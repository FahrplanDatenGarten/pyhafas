Code Structure
==============

Classes and methods
-------------------
pyHaFAS is build object-orientated with a lot of classes. You may know already the :class:`HafasClient <pyhafas.client.HafasClient>` and the profile classes but there a lot more classes for internal use only.
For example the :class:`BaseProfile <pyhafas.profile.base>` class consists among others of :class:`BaseRequestHelper <pyhafas.profile.base.helper.BaseRequestHelper>`, :class:`BaseJourneyRequest <pyhafas.profile.base.requests.BaseJourneyRequest>` and very important the :class:`ProfileInterface <pyhafas.profile.interfaces>`

Every class in a profile has a `Interface` which defines abstract methods that the profile class must implement.

A more detailed view of the construction of a profile is given on the page :doc:`profiles`.

File Structure
--------------
pyHaFAS's code is splitted in multiple files. This files are sorted as shown in the structure below.

* **/pyhafas** - base directory of source code

  * **profile** - contains the profiles (every subdirectory should have the same structure as `base`)

    * **interfaces** - contains all abstract classes
    * **base** - Base profile - contains the default handling classes and methods

      * **__init__.py** - contains the Profile
      * **helper** - contains helper functions that are used by multiple requests
      * **mappings** - contains mapping Enum classes
      * **requests** - contains code responsible for requests (there is a file for each request-type containing all methods belonging to it)

    * **PROFILENAME** - contains the files for the profile (only files and directories with changes)

  * **types** - Base directory of all types valid for all profiles

    * **exceptions.py** - excptions pyHaFAS can raise
    * **fptf.py** - most of the types important for pyHaFAS
    * **hafas_response.py** - contains  the :class:`HafasRepsonse <pyhafas.types.HafasResponse>` class

  * **client.py** - contains the :class:`HafasClient <pyhafas.client.HafasClient>`
