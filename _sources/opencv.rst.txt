Compiling Opencv
#################

We need to compile our own version of OpenCV 
to enable Gstream support, it helps us stream
video from camera over sockets.

Cloning the OpenCV repo
***********************

To Compile OpenCV we first need to clone the repo,
but since this project has included it as a submodule
we can just update the submodule and then compile it.

.. code-block:: bash

    git submodule update --init --recursive

This command will clone the opencv repo and all its 
submodules in the ``lib`` directory.

Compiling OpenCV
*******************
Now we can compile OpenCV

Go to the opencv directory
==========================

.. code-block:: bash

    cd lib/opencv-python

Set the cmake arguments
=======================

.. code-block:: bash

    export CMAKE_ARGS="-DWITH_GSTREAMER=ON"

Upgrade wheels (optional)
=========================

.. code-block:: bash

    pip install --upgrade pip wheel

Build OpenCV
==============

.. note:: 
    This step may take a while, depending on your machine.
    In the future I will add a docker image to have opencv
    precompiled with gstreamer support.

    You can add the ``--verbose`` flag to see the progress
    of the build process.

.. code-block:: bash

    pip wheel . --verbose

Add the wheels to the python path
=================================

.. code-block:: bash

    pip install opencv_python-*.whl

This command will install the opencv wheel and add it to the python path.
