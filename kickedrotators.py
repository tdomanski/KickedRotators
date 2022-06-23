# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def dphi1(phi1, phi2, tau, j, m, r):
  if m+phi1>1:
    m = m-m*np.floor(m+phi1)
  if phi1==j-tau:
    ret = r+m
  else:
    ret = r
  return ret

def dphi2(phi1, phi2, tau, i, M, R):
  if M+phi2>1:
    M = M-M*np.floor(M+phi2)
  if phi2==i-tau:
    ret = R+M
  else:
    ret = R
  return ret  

def func(z,t,m,M,r,R): 
    phi1, phi2 = z 
    return [dphi1(phi1,phi2,tau,t,m,r), dphi2(phi1,phi2,tau,t,M,R)] 

m=1
M=1

r = 8
R = 1
tau = 1

tmax = 1000
z0=[0,0]
t = np.linspace(0,tmax)
XX = odeint(func, z0, t, args=(m,M,r,R))
phi1 = XX[:, 0]
phi2 = XX[:, 1]
plt.plot(t,phi1)
plt.show()
plt.plot(t,phi2)
plt.show()
