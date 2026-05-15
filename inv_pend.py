import numpy as np
import matplotlib.pyplot as plt

g = 9.781987957
m = 1.5
M = 6
L = 1
I = m*L**2/3
F = 0
b = 1

t = 30
n = 1000
dt = t/n

tspan = np.linspace(0,t,n)
x0 = np.array([0,0,np.pi*.25,0])

x = np.zeros((n,4))
x[0,:] = x0

def inv_pend(x,F):
    dx0 = x[1]
    dx1 = (m**2*g*L**2*np.sin(x[2])*np.cos(x[2]) - I*(F + m*L*x[3]**2*np.sin(x[2]) - b*x[1]))/(m**2*L**2*(np.cos(x[2]))**2 - I*(M + m))
    dx2 = x[3]
    dx3 = m*L/I*(g*np.sin(x[2]) - np.cos(x[2])*dx1)
    return np.array([dx0,dx1,dx2,dx3])

for i in range(n-1):
    k1 = inv_pend(x[i,:],F)
    k2 = inv_pend(x[i,:] + dt/2*k1, F)
    k3 = inv_pend(x[i,:] + dt/2*k2, F)
    k4 = inv_pend(x[i,:] + dt*k3, F)
    x[i+1,:] = x[i,:] + dt/6*(k1 + 2*k2 + 2*k3 + k4)

plt.figure(figsize=(20,3))

for i in range(n):
    plt.clf()
    plt.plot([x[i,0],x[i,0]+L*np.sin(x[i,2])],[0,L*np.cos(x[i,2])])
    plt.text(-2,0.8,f"time = {tspan[i]:.2f} s")
    plt.ylim((-1.5,1.5))
    plt.xlim((-10,10))
    plt.pause(dt)

plt.show()