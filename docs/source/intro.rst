Basic setup
###########

This code has been tested majorly on linux systems, so if you are on windows
I recommend using `WSL2 <https://learn.microsoft.com/en-us/windows/wsl/install>`_,
and if you are on Mac OS then consider using a docker container with Ubuntu
installed.

Prerequisites
**************
Their are some Prerequisites that are needed for this project:

1. **Git** - To clone the repository and it's submodule (Very important without this
image capture won't work)

2. **Python 3.10** - I used ``Python 3.10`` for this project, and I recommend using
that only, don't know how the dependencies will behave with other version of python

3. **Docker** - Docker is required to run the simulation, you can run the simulation
without docker but setup of the `PX4 <https://px4.io/>`_ simulation stack is needed, I will have a guide
to that aswell so having docker is optional

4. **C/C++ Compiler** - A C/C++ compiler,specifically ``GCC`` to compile `OpenCV <https://opencv.org/>`_, 
yes we will be building ``OpenCV`` from source, as some features that we need are not enabled
in the ``pip`` distributed version.

5. **QGroundControl** - It is a groundcontrol station for drones, this can be used to manually control the
drone, come handy to check error logs or get the drone back to home location in case the aruco detection
goes haywire.

Go and install these dependencies, once done come back and clone the repository.

.. note::
    If you face any issue please contact me through the
    `github issue tracker <https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco/issues>`_, and tag
    `me <https://github.com/Witty-Wizard>`_

Cloning the repository
**********************

Installed all the dependencies? Great!! 

Now time to clone the repository on your system, for that run the following command. 

.. code-block:: bash

    git clone https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco.git --recursive

.. note::
    Notice that there is a ``--recursive`` flag in the clone command, this tells git to
    clone the base repositroy aswell as the submodule it might contain.
    
    Submodules are git repository inside other git repositories.

Now from this point you can take two approaches either start exploring the code base to
understand the working of the whole project, or simply start running the project
directly by following a step by step guide.

If you want to run the code as it is, go to the next page. Otherwise go to `this link <codeIntro.html>`_