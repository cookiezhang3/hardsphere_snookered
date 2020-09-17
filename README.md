# hardsphere_snookered
This project simulates a two-dimentional gas and animates it to illustrate and investigate the laws of thermodynamics. I use object-oriented programming (OOP) with Python programming language. I consider a perfect gas which is described by multiple balls bouncing inside a circular container. The animations are used for testing and debugging the programme. All the parts are working together to allow investigations on thermodynamics which includes the conservations law, ideal gas laws and velocitiy distributions.

![](https://github.com/cookiezhang3/hardsphere_snookered/blob/master/Sep-16-2020%2016-45-44.gif)

Here is a list of the files.

[hardsphere.py](https://github.com/cookiezhang3/hardsphere_snookered/blob/master/hard_spheres.py) : creates the Ball class and the Container class which inherits from Ball.

Simulation.py : initialises the systems and creates methods for collisions.

test_singleball_collide.py : tests the Simulation class for a single ball in a container.

test_balls_collide.py : visualises collisions between multiple balls in different cases.

theromo.py : investigates the conservation laws, the relations between variables and the velocity distribution through plots.

Note that I use Matplotlib Artist for the animations. You need to change the graphics backend to Tkinter for them to work properly. 
To do this: Tools -> Preferences -> IPython console -> graphics -> graphics backend and set it to Tkinter
