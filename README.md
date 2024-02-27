**DEXTER - LINE FOLLOWING ROBOT USING ROS2 HUMBLE IN classic gazebo**

OS AND SOFTWARE USED:

UBUNTU 22.04

ROS2 -HUMBLE

OPENCV

PROJECT DESCRIPTION:

Linefollower urdf is equipped with camera plugin which is used to get the image feed which is then bridged with openCV .Works by getting the mid point of line and robot, then the error between both values are used to send corresponding command velocity. 
  
Packages needed:
        
        sudo apt install ros-humble-xacro
        sudo apt install ros-humble-joint-state-publisher-gui
        sudo apt install ros-humble-gazebo-ros-pkgs

LAUNCHING COMMANDS:

In terminal 1:
                        
    ros2 launch dexter_des launch_sim.launch.py

![image](https://github.com/FERBIN12/dexter/assets/126778624/4f1c4eef-0c78-471c-8184-c4ea32b49636)


In terminal 2:

    ros2 run dexter_des line_follower_node

![image](https://github.com/FERBIN12/dexter/assets/126778624/fe7aa1f0-08f3-4f7c-a283-9cf193f13a70)


