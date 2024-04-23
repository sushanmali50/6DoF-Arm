# 6DoF Robot Arm Controller

## Overview

This repository contains the Python code for a simple graphical user interface (GUI) to control a 6 Degrees of Freedom (DoF) robot arm using a PCA9685 servo driver connected to a Raspberry Pi. The GUI allows individual control of each servo of the arm for testing and demonstration purposes.

## Features

- **Simple Control**: The GUI provides sliders to adjust the angle of each servo independently.
- **Grab Functionality**: Includes a 'GRAB' button to control the robot's grip.
- **Initialization Sequence**: On startup, the servos move to a default position.
- **Shutdown Sequence**: The program safely moves the servos to a rest position before shutting down.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need a Raspberry Pi setup with the PCA9685 servo driver connected to your 6DoF Robot Arm. The Python environment should have the necessary libraries installed, including `tkinter` for the GUI and `adafruit_servokit` for controlling the PCA9685 driver.

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/6dof-robot-arm-controller.git
```
2. Navigate to the cloned directory:
```bash
cd 6dof-robot-arm-controller
```
3. Run the script with the following command:
```bash
python3 robot_arm_controller.py
```
### Usage
After starting the script, the GUI will appear with the sliders. Move the sliders to control the servos' angles and press the 'GRAB' button to activate the grip mechanism.
![6DoF Robot Arm GUI] ![Screenshot 2024-04-23 124751](https://github.com/sushanmali50/6DoF-Arm/assets/145068266/96f572ee-0c54-41c0-befd-f884067e3c0e)

### Safety Notice
Before powering the servos, ensure they are correctly calibrated, and the robot arm is in a position that allows for the full range of motion without causing damage or injury.

## Current Work
I am currently working on integrating ROS2 control with this project. This will allow for more sophisticated control mechanisms using ROS2 packages, which will enable the robot arm to perform more complex tasks and be easily integrated into robotics projects that use the ROS2 ecosystem.

### Contributing
Feel free to fork the project, and submit pull requests, or open issues for suggestions and feature requests.
