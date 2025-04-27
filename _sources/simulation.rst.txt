Simulation
#####################

To run this simulation I am using PX4 that is a drone autopilot firmware,
which also provides Software-In-The-Loop (or SITL) support. 

To run the simulation you can either use the prebuild docker image 
that is included with this project under the ``docker`` directory, or 
you can clone `PX4 repository <https://github.com/PX4/PX4-Autopilot>`_ and run it directly

Running with docker
===================================================

I have made a docker image that will clone PX4 build it and then launch SITL.

First the image needs to be built for that run the following command:


Build the docker image
----------------------

.. code-block:: bash
    
    docker build --progress=plain -t px4-sitl ./docker

Then, run the simulation using the following command:

Run the container
-----------------

.. code-block:: bash

    docker compose up -d

.. note::
    The ``-d`` flag in docker compose is used to run the container in deteached state,
    meaning that the container keeps running in background and there is no need to keep
    the terminal open.


Now the SITL is runnning, try launching QGroundControl, it should auto connect to the
drone and you should be able to fly the drone using it.

Stopping the container
-------------------------
To stop the container run:

.. code-block:: bash

    docker compose down

.. important::
    Make sure to run ``docker compose`` command from the root directory of the repositroy
    otherwise it won't work

Running natively
===================================================
So, you don't want to use the container, fine, follow the following instructions to
setup PX4 and start simulation

Clone the repositroy
--------------------

Clone the PX4-Autopilot repository using the following command:

.. code-block:: bash

    git clone https://github.com/PX4/PX4-Autopilot.git --recursive --depth=1

.. note::
    the ``--depth=1`` flag ensures that only the last commit is cloned from the remote
    otherwise it would take a lot of time to clone the whole repository

Change directory
----------------

Now that the repository has been cloned, move inside the directory using:

.. code-block:: bash

    cd PX4-Autopilot

Installing dependencies
-----------------------

To build PX4 some tools are required, luckily they provide a script to install all the 
required dependencies. 

To install them run the following script:

.. code-block:: bash

    ./Tools/setup/ubuntu.sh --no-nuttx

.. note::
    If the script does not run then it might not have executable permissions, to fix it 
    run the following command:

    .. code-block:: bash

        chmod +x ./Tools/setup/ubuntu.sh

    Now run the script again

Running the simulation
----------------------

Now time to build and run the simulation, use the following command:

.. code-block:: bash

    make px4_sitl gz_x500_mono_cam_down

If you run this for the first time it will take some time as it is building the project
for the first time.

Once the build is done, the simulation will start on its own and you can use QGroundControl
to control the drone