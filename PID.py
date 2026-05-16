import numpy as np
import matplotlib.pyplot as plt

g = 9.781987957
m = 1.5
M = 6
L = 1
I = m*L**2/3
F = 0
b = 0.1

t = 20
n = 2000
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

Kc = -960
Ki = -500
Kd = -40

spx = 0

Kcx = 0.08
Kix = 0
Kdx = 0.038

int_ex = 0
int_e = 0

e_pre = 0

for i in range(n-1):
    x[i,2] %= 2*np.pi

    if x[i,2] > np.pi:
        x[i,2] -= 2*np.pi

    ex = spx - x[i,0]

    int_ex += dt*ex

    ex_der = -x[i,1]

    sp = Kcx*ex + Kix*int_ex + Kdx*ex_der
    sp = np.clip(sp,-0.3,0.3)
    e = sp - x[i,2]

    int_e += dt*e

    if i == 0:
        e_der = 0
    else:
        e_der = (e - e_pre)/dt
    e_pre = e

    F = Kc*e + Ki*int_e + Kd*e_der

    k1 = inv_pend(x[i,:],F)
    k2 = inv_pend(x[i,:] + dt/2*k1, F)
    k3 = inv_pend(x[i,:] + dt/2*k2, F)
    k4 = inv_pend(x[i,:] + dt*k3, F)
    x[i+1,:] = x[i,:] + dt/6*(k1 + 2*k2 + 2*k3 + k4)

plt.figure(figsize=(10,3))

for i in range(n):
    plt.clf()
    plt.plot([x[i,0],x[i,0]+L*np.sin(x[i,2])],[0,L*np.cos(x[i,2])])
    plt.text(-2,0.8,f"time = {tspan[i]:.2f} s")
    plt.ylim((-1.5,1.5))
    plt.xlim((-5,5))
    plt.pause(dt)

plt.show()