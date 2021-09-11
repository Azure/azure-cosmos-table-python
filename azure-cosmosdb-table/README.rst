Microsoft Azure CosmosDB Table SDK for Python
=============================================

**Please note, a newer package is available** `azure-data-tables`_ **as of June 2021.**

**While this package will continue to receive critical bug fixes, we strongly encourage you to upgrade. See** `Migration Guide`_ **for more details.**

This project provides a client library in Python that makes it easy to
consume Microsoft Azure CosmosDB Table services.

Please note, this library supports service version 2017-04-17 and below.


Compatibility
=============

**IMPORTANT**: If you have an earlier version of the azure package
(version < 1.0), you should uninstall it before installing this package.

You can check the version using pip:

.. code:: shell

    pip freeze

If you see azure==0.11.0 (or any version below 1.0), uninstall it first then install it again:

.. code:: shell

    pip uninstall azure
    pip install azure

Features
========

-  Table

   -  Create/Read/Update/Delete Tables
   -  Create/Read/Update/Delete Entities
   -  Batch operations
   -  Advanced Table Operations


Getting Started
===============

Download
--------

Option 1: Via PyPi
~~~~~~~~~~~~~~~~~~

To install via the Python Package Index (PyPI), type:

::

    pip install azure-cosmosdb-table

Option 2: Source Via Git
~~~~~~~~~~~~~~~~~~~~~~~~

To get the source code of the SDK via git just type:

::

    git clone git://github.com/Azure/azure-cosmosdb-python.git
    cd ./azure-cosmosdb-table
    python setup.py install

Option 3: Source Zip
~~~~~~~~~~~~~~~~~~~~

Download a zip of the code via GitHub or PyPi. Then, type:

::

    cd ./azure-cosmosdb-table
    python setup.py install


Minimum Requirements
--------------------

-  Python 2.7, 3.3, 3.4, 3.5, or 3.6.
-  See setup.py for dependencies

Usage
-----

To use this SDK to call Microsoft Azure storage services, you need to
first `create an account`_.

Code Sample
-----------

See the samples directory for table usage samples.

Need Help?
==========

Be sure to check out the Microsoft Azure `Developer Forums on MSDN`_ or
the `Developer Forums on Stack Overflow`_ if you have trouble with the
provided code.

Contribute Code or Provide Feedback
===================================

If you would like to become an active contributor to this project, please
follow the instructions provided in `Azure Projects Contribution
Guidelines`_. You can find more details for contributing in the `CONTRIBUTING.md doc`_.

If you encounter any bugs with the library, please file an issue in the
`Issues`_ section of the project.

Learn More
==========

-  `Python Developer Center`_
-  `Azure Storage Service`_
-  `Azure Storage Team Blog`_

.. _azure-data-tables: https://pypi.org/project/azure-data-tables/
.. _Migration Guide: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/tables/azure-data-tables/migration_guide.md
.. _Python Developer Center: http://azure.microsoft.com/en-us/develop/python/
.. _create an account: https://account.windowsazure.com/signup
.. _Developer Forums on MSDN: http://social.msdn.microsoft.com/Forums/windowsazure/en-US/home?forum=windowsazuredata
.. _Developer Forums on Stack Overflow: http://stackoverflow.com/questions/tagged/azure+windows-azure-storage
.. _Azure Projects Contribution Guidelines: http://azure.github.io/guidelines.html
.. _Issues: https://github.com/Azure/azure-cosmosdb-python/issues
.. _Azure Storage Service: http://azure.microsoft.com/en-us/documentation/services/storage/
.. _Azure Storage Team Blog: http://blogs.msdn.com/b/windowsazurestorage/
.. _CONTRIBUTING.md doc: CONTRIBUTING.md
