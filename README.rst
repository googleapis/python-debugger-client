Python Client for Google Cloud Debugger API
===========================================

|beta| |pypi| |versions|

`Cloud Debugger`_: is a feature of Google Cloud Platform that lets you inspect the state of an application, 
at any code location, without stopping or slowing down the running app. Cloud Debugger makes it easier to 
view the application state without adding logging statements.

- `Client Library Documentation`_
- `Product Documentation`_

.. |beta| image:: https://img.shields.io/badge/support-beta-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/master/README.rst#beta-support
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-debugger-client.svg
   :target: https://pypi.org/project/google-cloud-debugger-client/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-debugger-client.svg
   :target: https://pypi.org/project/google-cloud-debugger-client/
.. _Cloud Debugger: https://cloud.google.com/debugger/docs
.. _Client Library Documentation: https://googleapis.dev/python/clouddebugger/latest
.. _Product Documentation:  https://cloud.google.com/debugger/docs

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Cloud Debugger API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Cloud Debugger API.:  https://cloud.google.com/debugger/docs/setup/python#verifying_the_api_is_enabled
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-debugger-client


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-debugger-client

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Cloud Debugger
   to see other available methods on the client.
-  Read the `Cloud Debugger Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Cloud Debugger Product documentation:  https://cloud.google.com/debugger/docs
.. _README: https://github.com/googleapis/google-cloud-python/blob/master/README.rst