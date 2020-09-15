#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:08:00 2019

@author: keqizhang
"""
"""
testing next_collision for multiple balls
"""
import hard_spheres as hs
import Simulation as sl
import matplotlib.pyplot as plt

#%%
"""
check Simulation with two balls input (Task 7).
"""
b=[hs.Ball(1,1,[-5.,0.,0.],[1.,0.,0.]), hs.Ball(1,1,[4.,0.,0.],[-3.,0.,0.])
   ,hs.Contain(100000,10,[0.0,0.0,0.0],[0.0,0.0,0.0])]
trail=sl.Simulation(b)
trail.next_collision()
trail.run(100,True)

#%%
"""
velocity in x y direction
"""
b=[hs.Ball(1,1,[-5.,0.,0.],[1.,2.,0.]), hs.Ball(1,1,[4.,0.,0.],[-3.,3.,0.])
   ,hs.Contain(100000,10,[0.0,0.0,0.0],[0.0,0.0,0.0])]
trail=sl.Simulation(b)
trail.next_collision()
trail.run(100,True)

#%%
"""
check initialisation-group of balls (Task 8). 
"""
trail=sl.Simulation()
trail.next_collision()
trail.run(20,True)

#%%
"""
plotting histogram for ditance from centre (Task 9).
"""
trail=sl.Simulation()
trail.next_collision()
trail.run(50,False)
params = {
   'axes.labelsize': 18,
   'font.size': 18,
   'font.family': 'sans-serif', 
   'font.serif': 'Arial', 
   'legend.fontsize': 18,
   'xtick.labelsize': 16,
   'ytick.labelsize': 16, 
   'figure.figsize': [8.8, 8.8/1.618] 
} 
plt.rcParams.update(params)
plt.grid()
#print(hs.Simulation.distance_between)
#print(hs.Simulation.distance_to_centre)
print(len(trail.distance_to_centre),'TEST')
plt.hist(trail.distance_to_centre)
plt.xlabel('Distance to center(a.u.)')
plt.ylabel('Frequency')
plt.title('Distance to central postion')

"""
plotting histogram for ditance between balls
"""

plt.hist(trail.distance_between)
plt.xlabel('Distance between pair of balls(a.u.)')
plt.ylabel('Frequency')
plt.title('Distance between each pair of balls')

#plt.hist(hs.Simulation.distance_between)
plt.show()