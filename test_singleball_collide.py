# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:32:25 2019

@author: KZ1617
"""
"""
Testing the methods in the Ball class and the Container class; testing the 
Simulation class for a single ball. (Task 2-5)

"""
import singleball as sb
import hard_spheres as hs

#%%
'''
ball with velocity in x direction
'''
b=hs.Ball(1,1,[-5.,0.,0.],[1.,0.,0.])
c=hs.Contain(100000,10,[0.0,0.0,0.0],[0.0,0.0,0.0]) #mass of container great so it does not move 
trial=sb.Simulation(b,c)
trial.run(100,True)
print('time', trial.next_collision())
print(b.vel())

#%%
'''
ball with velocity in both x and y direction
'''
b=hs.Ball(1,1,[-5.,0.,0.],[1.,1.,0.])
c=hs.Contain(100000,10,[0.0,0.0,0.0],[0.0,0.0,0.0])
trial=sb.Simulation(b,c)
print('time', trial.next_collision())
print(b.vel())


        