import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imgp
import scipy.io
from scipy.io import loadmat
from scipy.signal import convolve2d

# Parameters
Re = 1500
tsim = 1
dt = 1e-5
nt = int(np.round(tsim/dt))

Lx = 1
Ly = 1
Nx = 1024
Ny = 1024
dx = Lx/Nx
dy = Ly/Ny

# Campo de velocidad
u = np.zeros((Nx+1, Ny+2)) # Eje x
v = np.zeros((Nx+2, Ny+1)) # Eje y

uce = np.zeros((Nx, Ny))
vce = np.zeros((Nx, Ny))

uce = (u[0:Nx, 1:Ny + 1] + u[1:Nx + 1, Ny + 1]) * 0.5
vce = (v[1:Nx + 1, 0:Ny] + v[1:Nx + 1, Ny + 1]) * 0.5

# Campo de presión
p = np.zeros((Nx, Ny))

W_h = np.array([
    [1],
    [-2],
    [1]
])

W_v = np.array([
    [1, -2, 1]
])

prom_x = np.array([
    [1],
    [1]
])

prom_y = np.array([
    [1, 1]
])

dvx = np.array([
    [-1],
    [1]
])

dvy = np.array([
    [-1, 1]
])