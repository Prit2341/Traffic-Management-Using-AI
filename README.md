<div align = "center">
 
# Traffic-Managment-Using-AI
  
[![Python version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python version](https://img.shields.io/badge/matplotlib-3.5.1-green.svg)](https://pypi.org/project/matplotlib/)
[![Python version](https://img.shields.io/badge/NEAT-0.92-yellow.svg)](https://pypi.org/project/neat-python/)
[![MATLAB](https://img.shields.io/badge/METLAB-gray.svg)](https://www.mathworks.com/products/matlab.html)
[![Python version](https://img.shields.io/badge/pygame-2.1.2-blue.svg)](https://pypi.org/project/pygame/)
 <p> Our Traffic Managment System Uses AI to Coordinate traffic such that people have to Spent the least time in traffic our AI coordinate between traffic signals to ensure people don't have signals to ensure people don't have to stop at multiple signals we use image detection to find traffic density and alot time dynamically to each lane</p>
</div>
 
 ## Problem Statment
 * Congestion is mainly due to the intensive use of automobiles, whose ownership has spread massively in Urban Area in recent decades
 * a lot of time gets wasted in traffic signals as the no of the vehicles is the less than expected
 * While driving through consecutive traffic signals we often have to  wait at each of the signal
 * Traffic Not only cause the extra delay but also increase fuel consumption, add transortatioin cost

## Customary Solutions
* **Manual Controlling** :- As the Name Suggests That's requires More ManPower to control Traffic and Traffic Police is alloted to each traffic signals and Traffic police has to control traffic
* **Automatic Controlling** :- Automatic Traffic Light is Controlled by the timer and electrical Sensors The Light are getting automatically Getting ON and OFF 
* **Electroinc Controlling** :- In Electronic Contrilling Method We have To placing some detector or sensors on the traffic area, and this sensors give data about the traffic Density and controll the traffic signals

## Drew back of the Customary Solution
* The Manual Controlling System is static and requires a large number of the manpower 
* They May cause a delay in the quick movement of traffic 
* Electronic Sensors and detector are very expensive in cost, accuracy and coverage are often in conflict 

## Proposed System
<p>The Traffic flow has no specific pattern that is followed, and the static signal timers pose a huge problem to the already critical problem of congestion</p>

<p>Therefore, we are implementing a system which aims to reduce chance of such scenarios by automatically computing the optimal green signal time based on the current traffic at the signal will ensure that the direction with more traffic is allotted a green signal for longer duration of time as compared to the direction with lesser traffic</p>

<p>So over dynamic traffic managment system can override the current static system which cause unwanted delays and congestion. also our system will also reduce the time complexity of vehicles pass.</p>

<p>The main objective of our system is to design an AI Based on Edge Computing that can Solve Current Traffic Situation Our System aims to use Image Recognization System and Live video feed from the CCTV Cameras at Traffic Junctions for calculating Real time traffic density and our AI Set the signal Time accordingly.</p>

## Advantages of the Our Traffic Management System
* Autonomous: There are no need of the Manpower
* Dynamic System, Mens Traffic light switching according to current traffic density
* less expensive than other solutions
* There are no need to new hardware to be installed

## Step by Step FlowChart of our Proposed System
Step 1 :- Caputuring Vehicles Image Using CCTV At Traffic Signals</br>
Step 2 :- Indetify The Vehicles and Calculate Number of the Vehicles</br>
Step 3 :- Send Final Number of the Vehicles to AI</br>
Step 4 :- AI Scheduling the Green Signal Time according to Traffic Density</br>
Step 5 :- Updating traffic Signal Time</br>

## Some of the Fectors That Our AI Considered  While Switching Traffic Signals
* The Processing Time of the  Image Recognization System to Calculate traffic Density
* Lag each vehicle suffers during start up
* Average speed each catagory of Vehicles
* The No. of Lanes

## Results
Here we Compare the Total Number of the Vehicles that crosses the intersection over 1 Simulation(5 Min) in the current system and Our implemented System With The random number of the Vehicles, Over A Total Time of 1 Hour With 12 Simulations of 5 Min each.  

## Installastion

All user Installastion
```
pip install neat-python
pip install pygame
```
for the Graph only
```
pip install matplotlib
```

For the Using NEAT Download the config.txt file from the Below Link</br>
Link :- https://techwithtim.net/wp-content/uploads/2019/08/config-feedforward.txt</br>
Save the Above file as config.txt 

## Visualization Of the Static Model
<p>Here we see in our static model that static time is given to each signal i.e. 30sec which leads to wastage of time when enough vehicles are not present in that lane. </p>

https://user-images.githubusercontent.com/83399207/166122672-41c9be4b-f215-4673-9019-69fec0b0b2e3.mp4

## Visualization Of the Dynamic Model
<p>In our dynamic model, using image detection we determine the traffic density in that lane and provide just enough time for the vehicles to pass which leads to time 
being saved in each of the lane and in each cycle. </p>

https://user-images.githubusercontent.com/83399207/166122642-451f48f1-028a-4911-adb0-2c7ab9ae892d.mp4



