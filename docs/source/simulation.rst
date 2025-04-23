Running Simulations
#####################


Docker
===================================================

.. code-block:: bash
    
    docker build --progress=plain -t px4-sitl ./docker

Then, run the simulation using the following command:

.. code-block:: bash

    docker compose up -d

or on non-unix like systems (windows 😒)

.. code-block:: bash

    docker-compose up -d

now the simulation is running open QGroundControl if you have
any doubt email me: 
`shashankmarch27@gmail.com <mailto:shashankmarch27@gmail.com>`_