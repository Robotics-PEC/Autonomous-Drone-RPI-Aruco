Understanding the Code
############################################

This codebase is designed to control a drone using ArUco marker detection
and PID-based control algorithms. The system processes video streams,
detects ArUco markers, calculates errors in position, and uses this data
to move the drone accordingly. Below, I'll explain each module, how they
interact, and the data flow within the system.

AdaAruco (ArUco Marker Detection)
*********************************

**File:** ``AdaAruco.py``

Purpose:
========

The AdaAruco module is responsible for detecting ArUco markers in the video stream. ArUco markers are used for visual localization and guidance of the drone.

Data Flow:
==========

- **Input:** Raw video frames from the AdaVideoStream class.
- **Processing:** The class detects ArUco markers in the frame and calculates their center based on the detected corners.
- **Output:** It outputs the center error of the detected ArUco markers relative to the center of the frame.

AdaVideoStream (Video Stream Handling)
**************************************

**File:** ``AdaVideoStream.py``

Purpose:
========

The AdaVideoStream class manages the retrieval of video frames from a UDP stream using the GStreamer library.

Data Flow:
==========

- **Input:** The UDP video stream (via GStreamer pipeline).
- **Processing:** GStreamer decodes the stream and provides frames for further processing.
- **Output:** The video frames are returned for marker detection or control.


AdaPIDController (PID Control)
*******************************

**File:** ``AdaController.py``

Purpose:
========

This module implements a PID (Proportional, Integral, Derivative) controller to calculate corrective actions based on the position errors of the drone.

Data Flow:
==========

- **Input:** Error values (e.g., position deviation from the center of the frame).
- **Processing:** The PID controller computes corrective values for movement.
- **Output:** Control signals that are sent to the drone.

AdaDroneController (Drone Control)
**********************************

**File:** ``AdaDroneControl.py``

Purpose:
========

The AdaDroneController class interfaces with the drone using MAVSDK, allowing for flight control such as arming, takeoff, movement, and landing.

Data Flow:
==========

- **Input:** Commands to arm, take off, move, and stop, based on the system’s state machine and sensor data.
- **Processing:** Sends commands to the drone through the MAVSDK library.
- **Output:** Controls the drone's movement based on the PID-controlled outputs.

AdaDebug (Logging and Debugging)
********************************

**File:** ``AdaDebug.py``

Purpose:
========

The AdaDebug module provides logging functionality to help track the flow of the system.

Data Flow:
==========

- **Input:** Log messages from various parts of the system.
- **Processing:** Logs messages to the console.
- **Output:** Provides visibility into the internal states of the system for debugging.

State Machine and Mission Control
**********************************

**File:** ``AdaVideoSteram.py``

Purpose:
========

This file manages the drone’s mission using a state machine (FSM_STATES), directing the drone through various phases like initialization, takeoff, movement, and landing.

Data Flow:
==========

- **Input:** Feedback from the ArUco marker detection system (position errors).
- **Processing:** The state machine controls the drone’s operations (e.g., takeoff, movement) based on the current state.
- **Output:** Commands to move or stop the drone, using the PID-controlled outputs.

Queue Management (AdaQueue)
===========================

**File:** ``AdaQueue.py``

Purpose:
=========

The queue is used for inter-thread communication between the video stream and the drone control system.

Data Flow:
===========

- **Input:** Results from the ArUco detection.
- **Processing:** These results are pushed to the queue for consumption by the main control loop.
- **Output:** The results are used to adjust the drone's position.