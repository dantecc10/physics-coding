# Código para simular dos planetas usando una
# ecuación diferencial ordinaria.

import numpy as np
import pygame
import matplotlib.pyplot as plt

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.font.init()
my_font = pygame.font.SysFont('Arial',10)
clock = pygame.time.Clock()
running = True
dt = 1/60
cn = 250

def rot(phi,tht,psi):
    # Esta función es para rotar objetos en 3D
    A = np.zeros((3,3))
    A[0,0] = np.cos(psi)*np.cos(tht)
    A[0,1] = np.cos(psi)*np.sin(tht)*np.sin(phi) -np.sin(psi)*np.cos(phi)
    A[0,2] = np.cos(psi)*np.sin(tht)*np.cos(phi) +np.sin(psi)*np.sin(phi)
    A[1,0] = np.sin(psi)*np.cos(tht)
    A[1,1] = np.sin(psi)*np.sin(tht)*np.sin(phi) +np.cos(psi)*np.cos(phi)
    A[1,2] = np.sin(psi)*np.sin(tht)*np.cos(phi) -np.cos(psi)*np.sin(phi)
    A[2,0] = -np.sin(tht)
    A[2,1] = np.cos(tht)*np.sin(phi)
    A[2,2] = np.cos(tht)*np.cos(phi)
    return A

def ode1(x,u,m):
    # variables de estado
    x1 = x[0] # Posición en el eje x de la masa
    x2 = x[1] # Velocidad en el eje x de la masa
    y1 = x[2] # Posición en el eje y de la masa
    y2 = x[3] # Velocidad en el eje y de la masa
    z1 = x[4] # Posición en el eje z de la masa
    z2 = x[5] # Velocidad en el eje z de la masa
    xp = np.zeros((6,1)) # xp indica derivada de x con respecto al tiempo dx/dt = xp
    xp[0] = x2
    xp[1] = (1/m)*( u[0] )
    xp[2] = y2
    xp[3] = (1/m)*( u[1] )
    xp[4] = z2
    xp[5] = (1/m)*( u[2] )
    return xp

class Masa:
    def __init__(self, position, speed, mass, color = (0, 0, 255), radius = 3):
        self.position = list(position)        
        self.speed = list(speed)
        self.mass = mass
        self.color = color
        self.radius = radius
    
#    def draw(self, screen):
#        x_axis = self.position[0]
#        y_axis = self.position[1]
#        print(x_axis, ", ", y_axis)
#        pygame.draw.circle(screen, self.color, [(x_axis, y_axis)], self.radius)

    def draw(self, screen):
        ppx = self.position[0] * mlt
        ppy = self.position[1] * mlt
        ppz = self.position[2] * mlt
        prx = ppx*R[0,0] + ppy*R[0,1] + ppz*R[0,2] + cn
        pry = ppx*R[1,0] + ppy*R[1,1] + ppz*R[1,2] + cn
        scralp4 = pygame.Surface((500,500), pygame.SRCALPHA)
        pygame.draw.circle(scralp4,(10,10,255,130), (prx,pry), 3)
        screen.blit(scralp4,(0,0))
        
    def move(self, u): # u es la fuerza ejercida por la otra masa
        self.u = u
        pos_array = [self.position[0], self.position[1], self.position[2]]
        speed_array = [self.speed[0], self.speed[1], self.speed[2]]
        data = np.concatenate((pos_array, speed_array))
        modifier = ode1(data, u, self.mass)
        self.position[0] = modifier[1]
        self.position[1] = modifier[3]
        self.position[2] = modifier[5]

# Constantes físicas
G = 1 #6.672e-11
v = np.sqrt((G*1e3)/(0.5*(10**3)))*5
print(v)

#variables masa 1
x1 = np.zeros((6,1))
x1[0,0] = -5 # Esta es la posición inicial en x
x1[3,0] = v  # Esta es la velocidad inicial en y
x1[2,0] = 0  # Posición incial en y
x1[4,0] = 0  # Posición incial en z
u1 = np.zeros((3,1))  # Aquí se va a colocar la fuerza ejercida por la otra masa
m1 = 1e3 # masa 1, su unidad son los kg
#variables masa 2
x2 = np.zeros((6,1))
x2[0,0] = 5  # Posición inicial en eje x
x2[3,0] = -v # Velocidd inicial en el eje y
x2[2,0] = 0  # Posición inicial en eje y
x2[4,0] = 0  # Posición inicial en eje z
u2 = np.zeros((3,1))
m2 = 1e3

u3 = np.zeros((3,1))
nueva_masa = Masa([cn, cn, 0], [5, -v, v], 1e3)


# varibles en común masas
d12 = 0                 # Distancia entre masas
u12 = np.zeros((3,1))   # Vector unitario

# Variables graficación
L = 50 # Distancia de los ejes del sistema de coordenadas cartesianas en 3D
a1 = 0  # Ángulo de rotación en eje x
a2 = 0  # Ángulo de rotación en eje y
a3 = 0  # Ángulo de rotación en eje z
ic = 1  # Variable auxiliar
mlt = 5 # Variable para amplificar distancia
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    # distancia entre masas
    d12 = np.sqrt((x1[0]-x2[0])**2+(x1[2]-x2[2])**2+(x1[4]-x2[4])**2)
    d13 = np.sqrt((x1[0]-nueva_masa.position[0])**2+(x1[2]-nueva_masa.position[1])**2+(x1[4]-x2[4])**2)
    d12 = np.sqrt((x1[0]-x2[0])**2+(x1[2]-x2[2])**2+(x1[4]-x2[4])**2)
    # Definición del vector unitario
    for k in range(3):
        u12[k] = (x1[2*k] - x2[2*k])/d12
    # Fuerza de atracción de las masas
    for k in range(3):
        u1[k] = -G*m1*m2*u12[k]*(1/(d12**2))
        u2[k] = -u1[k]
        u3[k] = -G*m1*m2*u12[k]*(1/(d13**2))
        

    # Solución de ecuación diferencial ordinaria para las masas
    hsim = 1/60 # paso de integración
    K11 = ode1(x1,u1,m1)
    K21 = ode1(x1+0.5*hsim*K11,u1,m1)
    K31 = ode1(x1+0.5*hsim*K21,u1,m1)
    K41 = ode1(x1+1.0*hsim*K31,u1,m1)
    x1  = x1 + (1/6)*hsim*(K11 + 2*K21 + 2*K31 + K41)
    K12 = ode1(x2,u2,m2)
    K22 = ode1(x2+0.5*hsim*K12,u2,m2)
    K32 = ode1(x2+0.5*hsim*K22,u2,m2)
    K42 = ode1(x2+1.0*hsim*K32,u2,m2)
    x2  = x2 + (1/6)*hsim*(K12 + 2*K22 + 2*K32 + K42)
    # Mostrar sistema de coordenadas cartesianas 3D
    R   = rot(a1,a2,a3)
    cn  = 250
    px  = L*R[0,0]
    py  = L*R[1,0]
    px2 = L*R[0,1]
    py2 = L*R[1,1]
    px3 = L*R[0,2]
    py3 = L*R[1,2]
    pygame.draw.aaline(screen,(255,0,0),[250,250],[px+cn,py+cn]  ,1)
    pygame.draw.aaline(screen,(0,255,0),[250,250], [px2+cn,py2+cn],1)
    pygame.draw.aaline(screen,(0,0,255),[250,250], [px3+cn,py3+cn],1)
    # Mostrar poligonos
    M  = 2*L
    px1 = cn
    py1 = cn
    px2 = M*R[0,0] + cn
    py2 = M*R[1,0] + cn
    px3 = M*R[0,0] + M*R[0,1] + cn
    py3 = M*R[1,0] + M*R[1,1] + cn
    px4 = M*R[0,1] + cn
    py4 = M*R[1,1] + cn
    px5 = M*R[0,1] + M*R[0,2] + cn
    py5 = M*R[1,1] + M*R[1,2] + cn
    px6 = M*R[0,2] + cn
    py6 = M*R[1,2] + cn
    px7 = M*R[0,0] + M*R[0,2] + cn
    py7 = M*R[1,0] + M*R[1,2] + cn
    px8 = M*R[0,0] + M*R[0,1] + M*R[0,2] + cn
    py8 = M*R[1,0] + M*R[1,1] + M*R[1,2] + cn
    scralp = pygame.Surface((500,500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp,(0,0,0,30), [[px1,py1],[px2,py2], [px3,py3],[px4,py4]],0)
    scralp2 = pygame.Surface((500,500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp2,(0,0,0,30), [[px1,py1],[px4,py4], [px5,py5],[px6,py6]],0)
    scralp3 = pygame.Surface((500,500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp3,(0,0,0,30), [[px1,py1],[px2,py2], [px7,py7],[px6,py6]],0)
    

    screen.blit(scralp,(0,0))
    screen.blit(scralp2,(0,0))
    screen.blit(scralp3,(0,0))
    # Mostrar masas
    ppx = x1[0,0] * mlt # Posición eje x
    ppy = x1[2,0] * mlt # Posición eje y
    ppz = x1[4,0] * mlt # Posición eje z
    prx = ppx*R[0,0] + ppy*R[0,1] + ppz*R[0,2] + cn
    pry = ppx*R[1,0] + ppy*R[1,1] + ppz*R[1,2] + cn
    scralp4 = pygame.Surface((500,500), pygame.SRCALPHA)
    pygame.draw.circle(scralp4,(10,10,255,130), (prx,pry),3)
    screen.blit(scralp4,(0,0))
    # Mostrar posición de masa m2
    ppx = x2[0,0] * mlt
    ppy = x2[2,0] * mlt
    ppz = x2[4,0] * mlt
    prx = ppx*R[0,0] + ppy*R[0,1] + ppz*R[0,2] + cn
    pry = ppx*R[1,0] + ppy*R[1,1] + ppz*R[1,2] + cn
    
    nueva_masa.move(u3)
    nueva_masa.draw(screen)
    
    
    scralp5 = pygame.Surface((500,500), pygame.SRCALPHA)
    pygame.draw.circle(scralp5,(10,10,255,130), (prx,pry),3)
    screen.blit(scralp5,(0,0))
    # Modificar orientación
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        a1 += ic*dt
    if keys[pygame.K_a]:
        a1 -= ic*dt
    if keys[pygame.K_w]:
        a2 += ic*dt
    if keys[pygame.K_s]:
        a2 -= ic*dt
    if keys[pygame.K_e]:
        a3 += ic*dt
    if keys[pygame.K_d]:
        a3 -= ic*dt
    if keys[pygame.K_r]:
        a1 = 0
        a2 = 0
        a3 = 0
    txt1 = my_font.render('Fuerza m1: ' +
    str(u1[0]) + str(u1[1]) + str(u1[2]), False, (0,0,0))
    txt2 = my_font.render('Fuerza m2: ' +
    str(u2[0]) + str(u2[1]) + str(u2[2]), False, (0,0,0))
    #txt3 = my_font.render('Fuerza m3: ')
    screen.blit(txt1,(10,0))
    screen.blit(txt2,(10,12))
    #screen.blit(txt3,(10,24))
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    # print(u1,u2)
    # running = False
pygame.quit()
