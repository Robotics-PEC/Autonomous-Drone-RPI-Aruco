.. ROS 101 documentation master file, created by
   sphinx-quickstart on Wed Apr  2 20:49:41 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Autonomous Drone RPI Aruco
===========================

.. raw:: html

    <p align="center">
        <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco/releases">
            <img src="https://img.shields.io/github/v/release/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="GitHub Release">
        </a>
        <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco/issues">
            <img src="https://img.shields.io/github/issues/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="GitHub Issues">
        </a>
        <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco">
            <img src="https://img.shields.io/github/stars/Robotics-PEC/Autonomous-Drone-RPI-Aruco?style=flat" alt="GitHub Stars">
        </a>
        <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
            <img src="https://img.shields.io/github/license/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="GitHub License">
        </a>
    </p>



Started this project in December of 2022 for Flipkart-Grid 4.0, none of us had
any clue what we were doing. We tried making our own FC using a teensy, tried
multiple python scripts and failed miserably.

Now fast forward to January 2024, tried to revisit this project, had learnt ROS
by then, still no luck the installation of ROS was complicated in itself so
never got to finish this again.

Today is April 2025, and I am writing this hoping that this time this would be
working and I would be able to create a first release of the project.

Autonomous Drone Aruco or **ADA** for short, I am going to use this term a lot
in this documentation, at the time of writing this documentation. All the
modules in the code work fine except the closed loop feedback control, and 
I will explain how to fix that and get it to work, I will also go through how
the code base is setup.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started:

   intro
   simulation
   opencv

.. toctree::
   :maxdepth: 2
   :caption: Code Explanation:

   codeIntro

Contributors
================

.. raw:: html

    <p align="center">
        <img alt="Current Creators" src="https://contrib.rocks/image?repo=Robotics-PEC/Autonomous-Drone-RPI-Aruco">
    </p>
