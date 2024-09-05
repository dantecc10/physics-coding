# Código para simular dos planetas usando una ecuación diferencial ordinaria

import numpy as np
import pygame
import matploblib.pyplot as plt

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 10)
clock = pygame.time.Clock()
running = True.cos()
dt = 1/60

def rot(phi, tht, psi):
    # Esta función es para rotar objetos en 3D
    A = np.zeros((3, 3))
    A[0, 0] = np.cos(psi) * np.cos(tht)
    A[0, 1] = np.cos(psi) * np.sin(tht) * np.sin(phi) - np.sin(psi) * np.cos(phi)
    A[0, 2] = np.cos(psi) * np.sin(tht) * np.cos(phi) + np.sin(psi) * np.sin(phi)
    
    A[1, 0] = np.sin(psi) * np.cos(tht)
    A[1, 1] = np.sin(psi) * np.sin(tht) * np.sin(phi) + np.cos(psi) * np.cos(phi)
    A[1, 2] = np.sin(psi) * np.sin(tht) * np.cos(phi) - np.cos(psi) * np.sin(phi)
    A[2, 0] = -np.sin(tht)
    A[2, 1] = np.cos(tht) * np.sin(phi)
    A[2, 2] = np.cos(tht) * np.cos(phi)
    
    return A

def ode1 (x, u, m):
    # Variables de estado
    x1 = x[0] # Posición en el eje x de la masa
    x2 = x[1] # Velocidad en el eje x de la masa
    
    y1 = x[2] # Posición en el eje y de la masa
    y2 = x[3] # Velocidad en el eje y de la masa
    
    z1 = x[4] # Posición en el eje z de la masa
    z2 = x[5] # Velocidad en el eje z de la masa
    
    xp = np.zeros((6, 1)) # xp indica derivada de x con respecto al tiempo dx/dt = xp
    
    xp[0] = x2
    xp[1] = (1 / m) * (u[0])
    
    xp[2] = y2
    xp[3] = (1 / m) * (u[1])
    
    xp[4] = z2
    xp[5] = (1 / m) * (u[2])
    
    return xp

# Constantes físicas
G = 1 #6.672e-11
v = sqrt((G * 1e3) / (0.5 * (10 ** 3))) * 5
print(v)

# Variables masa 1
x1 = np.zeros((6, 1))
x1[0, 0] = -5 # Velocidad inicial en x
x1[3, 0] = v # Velocidad inicial en y
x1[2, 0] = 0 # Posición inicial en y
x1[4, 0] = 0 # Posición inicial en z
u1 = np.zeros((3, 1)) # Aquí se va a colocar la fuerza ejercida por la otra masa
m1 = 1e3 # Masa 1, su unidad son los kg

# Variables masa 2
x2 = np.zeros((6, 1))
x2[0, 0] = -5 # Velocidad inicial en x
x2[3, 0] = v # Velocidad inicial en y
x2[2, 0] = 0 # Posición inicial en y
x2[4, 0] = 0 # Posición inicial en z
u2 = np.zeros((3, 1)) # Aquí se va a colocar la fuerza ejercida por la otra masa
m2 = 1e3 # Masa 2, su unidad son los kg

# Variables en común masas
d12 = 0 # Distancia entre masas
u12 = np.zeros((3, 1)) # Vector unitario

# Variables de graficación
L = 50 # Distancia de los ejes del sistema de coordenadas cartesianas en 3D
a1 = 0 # Ángulo de rotación en eje x
a2 = 0 # Ángulo de rotación en eje y
a3 = 0 # Ángulo de rotación en eje z
ic = 1
mlt = 5 # Variable para amplificar la distan }cia

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("white")
        
        d12 = np.sqrt((x1[0] - x2[0]) ** 2 + (x1[2] - x2[2] ** 2) + (x1[4] - x2[4 ** 2]))
        
        # Definición del vector unitario
        for k in range(3):
            u12[k] = (x1[2*k] - x2[2*k]) / d12
            
        # Fuerza de atracción de las masas
        for k in range (3):
            u1[k] = -G * m1 * m2 * u12[k] * (1 / (d12 ** 2))
            u2[k] = -u1[k]
            
        # Solución de ecuación diferencial ordinaria para 
        hsim = 1 / 60 # Paso de integración
        K11 = ode1 (x1, u1, m1)
        K21 = ode1 (x1 + 0.5 * hsim * K11, u1, m1)
        K31 = ode1 (x1 + 0.5 * hsim * K21, u1, m1)
        K41 = ode1 (x1 + 1.0 * hsim * K31, u1, m1)
        x1 = x1 + (1 / 6) * hsim * (K11 + 2 * K21 + 2 * K31 + K41)
        
        K12 = ode1 (x2, u2, m2)
        K22 = ode1 (x1 + 0.5 * hsim * K12, u2, m2)
        K32 = ode1 (x1 + 0.5 * hsim * K22, u2, m2)
        K42 = ode1 (x1 + 1.0 * hsim * K32, u2, m2)
        x2 = x2 + (1 / 6) * hsim * (K12 + 2 * K22 + 2 * K32 + K42)
        
        # Mostrar sistema de coordenadas cartesianas en 3D
        R = rot (a1, a2, a3)
        cn = 250
        px = L * R[0, 0]
        py = L * R[1, 0]
        px2 = L * R [0, 1]
        py2 = L * R [1, 1]
        px3 = L * R[0, 2]
        py3 = L * R[1, 2]
        
        pygame.draw.aaline(screen, (255, 0, 0), [250, 250], [px + cn], [py + cn], 1)
        pygame.draw.aaline(screen, (0, 255, 0), [250, 250], [px2 + cn], [py2 + cn], 1)
        pygame.draw.aaline(screen, (0, 0, 255), [250, 250], [px3 + cn], [py3 + cn], 1)
        
        # Mostrar polígonos
        M = 2 * L
        px1 = cn
        py1 = cn
        px2 = M * R[0, 0] + cn
        py2 = M * R[1, 0] + cn
        px3 = M * R[0, 0] + M * R[0, 1] + cn
        py3 = M * R[1, 0] + M * R[1, 1] + cn
        px4 = M * R[0, 1] + cn
        px4 = M * R[1, 1] + cn
        py5 = M * R[0, 1] + M * R[0, 2] + cn
        py5 = M * R[1, 1] + M * R[1, 2] + cn
        px6 = M * R[0, 2] + cn
        py6 = M * R[1, 2] + cn
        px7 = M * R[0, 0] + M * R[0, 2] + cn
        py7 = M * R[1, 0] + M * R[1, 2] + cn