# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:13:35 2019

@author: KZ1617
"""
import hard_spheres as hs
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

"""
The simulation class for a single ball inside a container.
"""

class Simulation:
    total_ke=[] 
    def __init__(self,ball,container):
        self._ball = ball
        self._container = container
        
    def next_collision(self):
        t=self._ball.time_to_collision(self._container)
        self._ball.move(t)
        self._ball.collide(self._container)  
        
    def run(self, num_frames, animate=False):
        if animate:
            f = pl.figure()
            ax = pl.axes(xlim=(-10, 10), ylim=(-10, 10))
            ax.add_artist(self._container.get_patch())
            ax.add_patch(self._ball.get_patch())
        for frame in range(num_frames):
            total=self._container.ke()+self._ball.ke()
            Simulation.total_ke.append(total)
            self.next_collision()
            if animate:
                pl.pause(0.01)
        if animate:
            pl.show()
    

    
    

        

   
        