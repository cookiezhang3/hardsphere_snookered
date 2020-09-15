#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:12:19 2019

@author: keqizhang
"""

import hard_spheres as hs
import numpy as np
import matplotlib.pyplot as plt

"""
here set up group of balls along the diagnals of a square in a container
for initialisation. Velocities are set at random interger between -400 and 
400 which is a typical range of gas molecules speed.
"""
iniballs=[hs.Contain(100000,10,[0.0,0.0,0.0],[0.0,0.0,0.0])]
xi=[-6]
yi=[5]
for i in range(1,6):
    xi.append(-6+2*i+0.1*i)
    yi.append(5-2*i-0.1*i)

for i in range(len(xi)):
    oneball=hs.Ball(1,1,[xi[i],yi[i],0],[np.random.randint(-400,400),np.random.randint(-400,400),0])
    secondball=hs.Ball(1,1,[-xi[i],yi[i],0],[np.random.randint(-400,400),np.random.randint(-400,400),0])
    iniballs.append(oneball)
    if i !=2 and i !=3 : #avoid overlapping at the centre
        iniballs.append(secondball)


class Simulation:

    def __init__(self,balls=iniballs):
        self._balls = balls
#        print('TEST',self._balls[1].pos())
        self.delmom = 0 #to count the total change in momentum
        self.total_time=0  #to count total simulation time
        self.total_pressure = 0
        self.total_ke = [] 
        self.total_mom=[]
        self.distance_to_centre = []
        self.distance_between = []
        self.position=[]
        self.velocity=[]
        self.speed=[]
        self.temp = 0
        
    def setvel(self):
        for i in range(len(self._balls[1:])):
            self._balls[i].v=np.array([np.random.randint(-400,400),
                       np.random.randint(-400,400),0], dtype="float64")
        
        """
        This method sets random veocities for the balls, which allows
        investigation of systems with different initial velocities/ KE.
        """
        
    def next_collision(self):
        p=[]
        for i in range(len(self._balls)):
            for j in range(len(self._balls)):
                if j<= i:
                    continue
                a=self._balls[i].time_to_collision(self._balls[j])
                #print(type(a))
                if a is not None:
                    p.append([a, self._balls[i], self._balls[j]])

        t1=[item[0] for item in p]
        t_min=min(t1)
 #       print(t_min)
        b=p[np.argmin(t1)] 

        for item in self._balls:
             item.move(t_min)
#             print(item.pos())
        b[2].collide(b[1])        
        self.total_time += t_min
#        print('test time', Simulation.total_time)
        if b[2].container== True:
            self.delmom += 2*b[1].m*np.sqrt(np.dot(b[2].vel(),b[2].vel()))

        elif b[1].container== True:
            self.delmom += 2*b[2].m*np.sqrt(np.dot(b[1].vel(),b[1].vel()))
            
        """
        This method loops over the possible collisions between each pair of 
        balls or a container, finds the minimum time for the next collision
        and performs the collision. It also counts the total time of a 
        simulation and the total change of momentum between ball-container 
        collision for later pressure calculation.
        """


    def data(self):
        keall=0 #the collection of ke of all balls
        momall=0
        for ball in self._balls:
            keall += ball.ke()
            momall += ball.mom()
                        
            if ball.container == False:
                self.position.append(ball.pos())
                self.velocity.append(ball.vel())
                self.speed.append(np.sqrt(np.dot(ball.vel(),ball.vel())))
        
        self.total_ke.append(keall/len(self._balls))  #average ke of the system
        self.total_mom.append(momall/len(self._balls)) #average mometum 

        """
        I check the conservation ke and momentum here as well as collecting 
        data of the position and speed of the balls to investigate velocity
        distribution.
        """

    def run(self, num_frames, animate=False):
 
        if animate:
            f = plt.figure()
            ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
            
            for item in self._balls:
                ax.add_artist(item.get_patch())
           
        for frame in range(num_frames):

            self.next_collision()
            self.data()

            if frame==num_frames-1:
                
                for i in range(len(self._balls)):
                    pos=self._balls[i].pos()
                    for j in range(len(self._balls)):
                        r=self._balls[i].r-self._balls[j].r 
                        self.distance_between.append(np.dot(r,r)**0.5)
                    self.distance_to_centre.append(np.dot(pos,pos)**0.5)

                self.temp = self.total_ke[0] / 1.38e-23 
                self.total_pressure=self.delmom/(self.total_time*np.pi*1)
                #print("CHECK", self.total_pressure, self.delmom/(self.total_time*np.pi*1))
                
            if animate:
                plt.pause(0.1)
        if animate:
            plt.show()

        """
        This method produces animation of the system. It performs one collsion 
        and collect one set of data in each frame. I calculate the temperature
        and pressure at the last frame.
        """

        
    
    
