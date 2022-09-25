<div align = "center">
 
# Traffic-Management-Using-AI
  
[![Python version](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python version](https://img.shields.io/badge/matplotlib-3.5.1-green.svg)](https://pypi.org/project/matplotlib/)
[![Python version](https://img.shields.io/badge/NEAT-0.92-yellow.svg)](https://pypi.org/project/neat-python/)
[![MATLAB](https://img.shields.io/badge/MATLAB-gray.svg)](https://www.mathworks.com/products/matlab.html)
[![Python version](https://img.shields.io/badge/pygame-2.1.2-blue.svg)](https://pypi.org/project/pygame/)
 <p> Our Traffic Management System Uses AI to Coordinate traffic such that people have to Spent the least time in traffic. Our AI coordinate between traffic signals to ensure people don't have to stop at multiple signals. We use image detection to find traffic density and allot time dynamically to each lane.</p>
</div>
 
 ## Problem Statement
 * Congestion is mainly due to the intensive use of automobiles, whose ownership has spread massively in Urban Area in recent decades.
 * A lot of time gets wasted in traffic signals as the no. of the vehicles is the less than expected.
 * While driving through consecutive traffic signals we often have to wait at each of the signal.
 * Traffic Not only cause the extra delay but also increase fuel consumption, and transportation cost.

## Customary Solutions
* **Manual Controlling** :- As the Name Suggests That's requires More ManPower to control Traffic and Traffic Police is alloted to each traffic signals and they have to control traffic.
* **Automatic Controlling** :- Automatic Traffic Light is Controlled by the timer and electrical Sensors. The Light are getting automatically Getting ON and OFF. 
* **Electronic Controlling** :- In Electronic Contrilling Method We have To placing some detector or sensors on the traffic area, and this sensors give data about the traffic Density and controll the traffic signals.

## Drawbacks of the Customary Solution
* The Manual Controlling System is static and requires a large number of manpower.
* They May cause a delay in the quick movement of traffic.
* Electronic Sensors and detector are very expensive in cost, accuracy and coverage are often in conflict. 

## Proposed System
<p>The Traffic flow has no specific pattern that is followed, and the static signal timers pose a huge problem to the already critical problem of congestion.</p>

<p>Therefore, we are implementing a system which aims to reduce chance of such scenarios by automatically computing the optimal green signal time based on the current traffic at the signal will ensure that the direction with more traffic is allotted a green signal for longer duration of time as compared to the direction with lesser traffic.</p>

<p>So our dynamic traffic management system can override the current static system which cause unwanted delays and congestion. also our system will also reduce the time complexity of vehicles pass.</p>

<p>The main objective of our system is to design an AI Based on Edge Computing that can Solve Current Traffic Situation Our System aims to use Image Recognization System and Live video feed from the CCTV Cameras at Traffic Junctions for calculating Real time traffic density and our AI Set the signal Time accordingly.</p>

## Advantages of the Our Traffic Management System
* Autonomous: There are no need of the Manpower
* Dynamic System, Manages Traffic light switching according to current traffic density.
* Less expensive than other solutions.
* There are no need to new hardware to be installed.

## Step by Step FlowChart of our Proposed System
Step 1 :- Capturing Vehicles Image Using CCTV At Traffic Signals</br>
Step 2 :- Indetify The Vehicles and Calculate Number of the Vehicles</br>
Step 3 :- Send Final Number of the Vehicles to AI</br>
Step 4 :- AI Scheduling the Green Signal Time according to Traffic Density</br>
Step 5 :- Updating traffic Signal Time</br>

## Some of the Factors That Our AI Considered  While Switching Traffic Signals
* The Processing Time of the Image Recognization System to Calculate traffic Density.
* Lag each vehicle suffers during start up.
* Average speed each catagory of Vehicles.
* The no. of Lanes.

## Installation

All user Installation
```
pip install neat-python
pip install pygame
```
for the Graph only
```
pip install matplotlib
```

Run the Python File
```
python simulation.py
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

## Results
Here we Compare the Total Number of the Vehicles that crosses the intersection over 1 Simulation(5 Min.) in the current system and Our implemented System With The random number of the Vehicles, Over A Total Time of 1 Hour With 12 Simulations of 5 Minutes each.  

![Comparison](https://user-images.githubusercontent.com/83399207/166123300-80854b3e-3da2-446d-87a5-b07aa1595325.png)

## Graph Representation
<p>As we can see with all conditions alike, our dynamic system was able to pass 3193 Vehicles while the current static system could pass only 2356 in 1 hour which means 837 more vehicles.

 Thus our proposed Traffic managment system with AI improves the performance by over 35%.
 
 Our proposed system on and average allow 70 more vehicles to pass every one simulation(5 min) aas compared to the current system this implies a reduction in time complexity of green signal time(Signal is green but no vehiclea passes) as well as the waiting time of the vehicles.
</p>

![graph](https://user-images.githubusercontent.com/83399207/166123319-a8e4a219-3ec0-4d55-9fd1-607147ea2d7e.png)
## NEAT AI
### Working of NEAT AI



![1](https://user-images.githubusercontent.com/83399207/166124081-42d7b3b2-f355-465a-9fae-dac8cff24043.jpg)
![2](https://user-images.githubusercontent.com/83399207/166124084-84de468e-f0c4-471a-b7c8-23db6680f1ab.jpg)
![3](https://user-images.githubusercontent.com/83399207/166124086-1a5d9c4b-4faf-45a8-a431-0c9cf631c871.jpg)
![4](https://user-images.githubusercontent.com/83399207/166124091-2e9a53e0-9658-44c7-8f94-518787e48e97.jpg)
![5](https://user-images.githubusercontent.com/83399207/166124089-18e2785f-6d9e-4422-9167-6e4fd107e662.jpg)
![6](https://user-images.githubusercontent.com/83399207/166124090-74ff8b01-9fb5-4476-85e0-5d6327c1b0c4.jpg)

## Graphical visualization of AI
The following video shows how the AI will coordinate the signals so that the vehicles will not have to stop at every signal if they want to travel on the same straight route.

https://user-images.githubusercontent.com/83399207/166124009-7ae31ef1-dd3f-4070-b77b-f8539402f355.mp4

### Conclusion
- Using the dynamic model we can effectively reduce the waiting time of the vehicles.
- Our proposed Traffic management system with AI improves the performance by over 35% comaparing to Current System.
- Using the AI model adds an additional functionality to reduce the waiting time of vehicles at their next crossing.
- Both of these can be implemented using edge computing at the traffic signal itself.
- It can be implemented with effectively with very little cost.   
