
## Setup
Clone the repository into your workspace and make 
```
git clone https://github.com/Abhishek2-2/task.git
```
Launch the main file. The robot should spawn in a warehouse environment
```
roslaunch ar1_description main.launch
```
To launch navigation
```
roslaunch ar1_navigation ar1_navigation.launch

roslaunch ar1_navigation task.launch
```
## About the Robot
- The main frame of reference is 'base_link'
- The robot has only 1 sensor and it publlishes its data to the /scan topic
- The drive topic of the robot is '/cmd_vel'
- The odometry topic and frame are 'odom'
- The footprint of the robot is 810mmx510mm with 'base_link' at its center
