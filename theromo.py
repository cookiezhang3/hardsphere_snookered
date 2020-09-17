#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:00:04 2019


@author: keqizhang
"""
"""
thermodynamics investigation
"""

import hard_spheres as hs
import Simulation as sl
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import moment


trail=sl.Simulation()
trail.next_collision()
trail.run(1000,False)
#print(trail.total_ke)
#print(trail.temp)
#print(trail.total_pressure)
#print(trail._balls[2].vel())
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

#%%
"""
check conservation of KE.
"""

#plt.grid()
plt.xlabel('t (a.u.)')
plt.ylabel('KE (a.u.)')
plt.title('Total Kinetic Energy vs time')
plt.plot(trail.total_ke)
plt.show()

#%%
"""
check conservation of momentum.
"""
abs_totalmom=[]
for i in range(len(trail.total_mom)-1):
    abs_totalmom.append(np.dot(trail.total_mom[i],trail.total_mom[i+1]))
plt.xlabel('t (a.u.)')
plt.ylabel('KE (a.u.)')
plt.title('Total Momentum vs time')
plt.plot(abs_totalmom)

#%%
"""
Run 15 simulation with different initial velocities. Plot the relationship
between pressure and temperature.
"""
    
P1=np.zeros(15)
T1=np.zeros(15)
for i in range(len(P1)):
    traili=sl.Simulation()
    traili.setvel()
    traili.run(1000,False)
    P1[i]=traili.total_pressure
    T1[i]=traili.temp
P1=sorted(P1)
T1=np.array(sorted(T1))* 1.38e-23 
fit,cov=np.polyfit(T1,P1,1,w=None,cov=True)
z=np.poly1d(fit)
plt.ylabel('Pressure (a.u.)')
plt.xlabel('Temperature (a.u.)')
plt.title('Pressure vs Temperature')
plt.plot(T1,P1, 'ro')
plt.plot(T1,z(T1))

"""
Investigate the gradient of the P-T graph with greater volume.
"""
P2=np.zeros(15)
T2=np.zeros(15)
for i in range(len(P2)):
    traili=sl.Simulation()
    traili._balls[0].R=20
    traili.setvel()
    traili.run(1000,False)
    P2[i]=traili.total_pressure
    T2[i]=traili.temp
P2=sorted(P2)
T2=np.array(sorted(T2))* 1.38e-23 
fit,cov=np.polyfit(T2,P2,1,w=None,cov=True)
z=np.poly1d(fit)
plt.plot(T2,P2, 'ro')
plt.plot(T2,z(T2))

plt.show()

#%%
"""
Compare the velocity distribution to Maxwell-Boltzmann distribution. The 
2D Maxwell function is defined here. The varience and mean velocity of both
the histogram and the Maxwell-Boltzmann distribution at this temperature are
calculated.
"""
m=1
T=trail.temp
kB=1.3806503e-23

def fmb(m,T,v):
    return m*v * np.exp((-m*v*v)/(2.*kB*T))/(kB*T)

v=np.array(trail.speed, dtype='float64')
v = np.array(sorted(trail.speed), dtype='float64')
print(v[0])
print(fmb(m,T,v)[0])
plt.xlabel('velocities (a.u.)')
plt.ylabel('probability density ')
plt.text(400,0.0025, r'$f(v)=\frac{m}{k_{B}T} v \exp[{\frac{-mv^{2}}{2k_{B}T}}]$', fontsize=16, color='g')
plt.title('Distribution of Velocities')
plt.plot(v,fmb(m,T,v))
plt.hist(v, density=True)
plt.show()

a=np.sqrt(kB*T/m)
maxvar=a**2*(3*np.pi-8)/np.pi
maxmean=2*a*np.sqrt(2/np.pi)
print('vmean',v.mean())
print('maxmean',maxmean)
print('vvar',stats.moment(v,moment=2))
print('maxvar',maxvar)





