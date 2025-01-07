
# RT1 Assignment 2 PT2 - Robot Control Package in ROS2

This assignment involves the implementation of a ROS2 package that allows controlling a robot in the environment where it was spawned. The command given by the user will be executed for one second, after which the user can enter a new command.

## Prerequisites

- ROS2 environment installed and configured
- `robot-urdf` package

To clone the `robot-urdf` package, you can use the folliwing command line in your workspace:  
```bash
git clone https://github.com/CarmineD8/robot_urdf.git
```


## Package Overview

This package contains a single Python node that allows the user to control the robot's movement by setting the following velocities:

- **Linear velocity along X**
- **Linear velocity along Y**
- **Angular velocity along Z**

## Running the Code

To run the code, follow these steps:

### 1. Launch the Gazebo simulation

In your first terminal, run the following command to launch the simulation from the `launch` directory:

```bash
ros2 launch gazebo.launch.py
```

### 2. Run the robot controller node

In another terminal, run the following command to start the robot control node:

```bash
ros2 run turtlebot_controller turtlebot_controller
```

This will allow you to send commands to the robot. The velocities will be applied for one second, and after that, you can input a new command.

