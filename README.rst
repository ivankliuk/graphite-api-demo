==============================
Custom finder for Graphite API
==============================

This project is a proof of concept, per se. It consists of three entities:

* Custom finder for Graphite API
* Graphite API server entry point
* Data Source server


Workflow
--------

Custom finder is installed into Graphite API system by adding corresponding lines info ``config.yaml`` (it's already done for you). The finder has only one function: fetching data from Data Source server which appears as a simple single-threaded one and returns random data in JSON format.

Installation
------------

Installation instruction presumes you're using ``virtualenv`` and ``pip`` for managing Python packages. Please note, the project works on Python 2.7+ only.

#. Download project from GitHub:

   .. code :: bash

      git clone https://github.com/ivankliuk/graphite-api-demo.git

#. Change current directory:

   .. code :: bash

      cd graphite-api-demo/

#. Create Python ``virtualenv``:

   .. code :: bash

      mkvirtualenv graphite

#. Install project's requirements and ``graphite-api-plugin``:

   .. code :: bash

      pip install -r requirements.txt
      python setup.py install

Execution
---------

If you want to use predefined paths, IP addresses and ports just run:

.. code :: bash

      chmod +x run.sh
      ./run.sh

Configuration
-------------

If you want to use custom paths, IP addresses and ports, please follow these steps:

#. You have to set ``GRAPHITE_API_CONFIG``. It should point where Graphite API config file is located. For instance:

.. code :: bash

  export GRAPHITE_API_CONFIG=${HOME}/graphite_api_demo/config.yaml

#. To start both Graphite API and Data Source servers execute following commands:

.. code :: bash

   python graphite_api_server.py <HOST> <PORT1> &
   python data_source_server.py <HOST> <PORT2> &

where ``HOST``, ``PORT1`` and ``PORT2`` IP address and ports where servers will be listening.
