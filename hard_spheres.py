# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:13:35 2019

@author: KZ1617
"""
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


class Ball:

    def __init__(self,m,R,r=[0.0,0.0,0.0],v=[0.0,0.0,0.0]):
        self.m=m
        self.R=R
        self.r=np.array(r)
        self.v=np.array(v)
        self.patch=pl.Circle(self.r, self.R, fc='r')
        self.container=False

    def setball(self,m,R,r,v):
        self.m=m
        self.R=R
        self.r=np.array(r)
        self.v=np.array(v)
        
    def pos(self):
        return self.r
    
    def vel(self):
        return self.v
    
    def get_patch(self):
        return self.patch
    
    def ke(self):
        return 0.5*self.m*np.dot(self.v,self.v)#self.ke
        
    def mom(self):
        return self.m*self.v
     
    def move(self,dt):
        a=self.r+self.v * dt
        self.r=a
        self.patch.center = self.r
        
    def time_to_collision(self,other):
        r=self.r-other.r 
        v=self.v-other.v
#        print('test',r,v)#the relative velocity
        
        if self.container==True:
            R=self.R-other.R 
        elif other.container==True:
            R=other.R-self.R
        else:
            R=self.R+other.R
            
        d=np.dot(r,v) 
        root=d**2-(np.dot(v,v))*(np.dot(r,r)-R**2)
        
        if root >= 0 and np.dot(v,v) != 0: 
            #ignore the v.v=0 case makes no physical difference.
            t1=(-d-(root)**0.5)/np.dot(v,v)
            t2=(-d+(root)**0.5)/np.dot(v,v)
            
            if t1 < t2 and t1 >= 0:
                return t1*0.98 
            #facotr of 0.98 fix counting error of computer
            elif  t2 >= 0:
                return t2*0.98
            else:
                return None         
        else:
            return None       
        
        """
        This method calculate the time until the next collision. Making an 
        distinguishment between ball-ball and ball-container collision. 
        """
            
    def collide(self,other):
        v=self.v-other.v
        r=self.r-other.r
        r_mag_square=np.dot(r,r)
        m1=self.m
        m2=other.m
        v1=self.v - 2*np.dot(v,r)*m2*r/((m1+m2)*r_mag_square)
        v2=other.v + 2*np.dot(v,r)*m1*r/((m1+m2)*r_mag_square)
        self.v=v1 
        other.v=v2
        #print(r)
        
        """
        this method make the changes to the velocities of the ball and the 
        other one due to collision.
        """

class Contain(Ball):
    
    def __init__(self,m,R,r=[0.0,0.0,0.0],v=[0.0,0.0,0.0]):
        Ball.__init__(self,m,R,r=[0.,0.,0.],v=[0.,0.,0.])
        self.patch=pl.Circle(self.r, self.R, ec='b', fill=False, ls='solid')
        self.container=True

    """
    The Contain class is inherited from the Ball class. A container has almost 
    the same properties of a ball except that it has great mass and radius.
    """


        
    
    

        

   
        