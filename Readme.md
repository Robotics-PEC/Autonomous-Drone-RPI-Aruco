<p align="center">
    <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco/releases"><img src="https://img.shields.io/github/v/release/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="GitHub Release"></a>
    <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco/issues"><img src="https://img.shields.io/github/issues/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="Github Issues"></a>
    <a href="https://github.com/Robotics-PEC/Autonomous-Drone-RPI-Aruco"><img src="https://img.shields.io/github/stars/Robotics-PEC/Autonomous-Drone-RPI-Aruco?style=flat
    " alt="GitHub Stars"></a>
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html"><img src="https://img.shields.io/github/license/Robotics-PEC/Autonomous-Drone-RPI-Aruco" alt="GitHub License"></a>
</p>

# Autonomus Drone RPI

Started this project in December of 2022 for Flipkart-Grid 4.0, none of us had
any clue what we were doing. We tried making our own FC using a teensy,
tried multiple python scripts and failed miserably.

Now fast forward to January 2024, tried to revisit this project, had learnt
ROS by then, still no luck the installation of ROS was complicated in
itself so never got to finish this again.

Today is April 2025, and I am writing this hoping that this time this would
be working and I would be able to create a first release of the project.

## Getting Started

### TL;DR

Visit the documentation hosted on [this link](http://www.roboticspec.com/Autonomous-Drone-RPI-Aruco/), build using
[sphinx](https://www.sphinx-doc.org/en/master/)

### Simulation

First of all I don't have any hardware on hand so all the code will be
tested in a simulation enviornment. For simulating the drone I am
going to use PX4 SITL which is a autopilot software that also provides
simulation support, and for simulating the world I am using gazebo.

> [!NOTE]  
> The newer Gazebo Harmonic is now decoupled from ROS2, meaning that
> it can be used for simulation without the need for ROS installed
> I am not going to use ROS in this project for reasons mentioned
> above.

### Commanding the drone

For controlling the drone I am using `MAVSDK`, it is a library for
`mavlink` communication (the protocol between drone and Ground Station)

### Aruco detection

To detect aruco markers, I am sticking to the original idea of using opencv
getting their co-ordinates and then aligning the image frame with the
center of the aruco marker using a closed-loop control algorithm,
most likely PID.

### Future scopes

These are some Ideas that I have in mind but might not implement, as that
would increase the scope of project and require more effort.

- [ ] Vision based slam - I am using a monocular camera, and in indoor
enviornment where GPS is not available, an alternative odometry system is required, so vision based SLAM is used, their are many SLAM algorithms: ORB-SLAm, LSD-SLAM, DSO, SVO, DynaSLAM and many more

- [ ] Creating a GUI for the code - For now I have made a staic code that uses a CLI approach, in future it might be more beneficial to add a GUI interface, using either electron, QT with C++, or python (Choose your poison).

- [ ] Build the actual drone - Actually build the drone and check how it behaves in real life situations.

### Terminologies

- **Aruco**  
  ArUco is a library for detecting and tracking square fiducial markers. These markers are often used in robotics and computer vision for camera calibration, localization, and augmented reality applications.

- **MAVLink**  
  MAVLink (Micro Air Vehicle Link) is a lightweight messaging protocol for communicating with drones and between onboard drone components. It’s commonly used in systems like PX4 and ArduPilot.

- **Odometry**  
  Odometry is the process of estimating a robot's position and orientation over time using data from motion sensors like wheel encoders or visual inputs (visual odometry).

- **PID**  
  PID (Proportional–Integral–Derivative) is a type of feedback control system used to maintain a desired output by correcting errors between the setpoint and measured process variable.

- **PX4**  
  PX4 is an open-source flight control software for drones and other unmanned vehicles. It supports a wide range of hardware and offers features like autonomous flight, mission planning, and more.

- **SDK**  
  SDK (Software Development Kit) is a collection of software tools, libraries, and documentation that developers use to build applications for a specific platform or framework, such as a drone API.

- **SITL**  
  SITL (Software-In-The-Loop) is a simulation environment that allows developers to test flight control software without real hardware by running the flight stack on a computer and simulating the drone's sensors and environment.

- **SLAM**  
  SLAM (Simultaneous Localization and Mapping) is a technique used in robotics and autonomous systems to build a map of an unknown environment while simultaneously keeping track of the robot's location within it.

## Our Teams Members

<p align="center">
    <img alt="Current Creators" src="https://contrib.rocks/image?repo=Robotics-PEC/Autonomous-Drone-RPI-Aruco">
</p>

- [Mansi Kalra](https://github.com/mansi104-ai)
- [Reeshav Chowdhury](https://github.com/rishi18722)
- [Soumil Arora](https://github.com/TheSoumilArora)
- [Shashank Agarwal](https://github.com/Witty-Wizard)
- [Rishab Sood](https://github.com/RishabhSoodDSEE)
- [Ansh Chawla](https://github.com/anshchawla521)
- [Aayush Singla](https://github.com/Aayush052)
- Vinayak Pandey
