import numpy as np
import pygame

# This file contains several common functions used
# in the physics implementations in Python

# b = [L, cn, a1, a2, a3, mlt, dt]
# mass class creation
class mass:
    def __init__(self, pos, vel, forc, m):
        self.pos = list(pos)
        self.vel = list(vel)
        self.forc = list(forc)
        self.m = m
        
    def mkxp(self):
        x = np.zeros((6, 1))
        x[0, 0] = self.pos[0]
        x[2, 0] = self.pos[1]
        x[4, 0] = self.pos[2]
        x[1, 0] = self.vel[0]
        x[3, 0] = self.vel[1]
        x[5, 0] = self.vel[2]
        return x, self.m, self.forc

# Rotation matrix declaration
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

# Ordinary differential equation for the planets
def ode1(x, u, m):
    # Variables de estado
    x1 = x[0] # Posición en el eje x de la masa
    x2 = x[1] # Velocidad en el eje x de la masa
    y1 = x[2] # Posición en el eje y de la masa
    y2 = x[3] # Velocidad en el eje y de la masa
    z1 = x[4] # Posición en el eje z de la masa
    z2 = x[5] # Velocidad en el eje z de la masa
    xp = np.zeros((6, 1)) # xp indica la derivada de x con respecto al tiempo dx/dt = xp

    xp[] = x2
    xp[] = (1 / m) * (u[0])
    xp[] = y2
    xp[] = (1 / m) * (u[1])
    xp[] = z2
    xp[] = (1 / m) * (u[2])
    return xp

# Ordinary differential equation for the planets with body restrictions
def ode2(x, u, m):
    # Variables de estado
    x1 = x[0] # Posición en el eje x de la masa
    x2 = x[1] # Velocidad en el eje x de la masa
    y1 = x[2] # Posición en el eje y de la masa
    y2 = x[3] # Velocidad en el eje y de la masa
    z1 = x[4] # Posición en el eje z de la masa
    z2 = x[5] # Velocidad en el eje z de la masa
    xp = np.zeros((6, 1)) # xp indica la derivada de x con respecto al tiempo dx/dt = xp

    kv = 1000
    
    xp[] = x2
    xp[] = (1 / m) * (u[0] - kv * x[1])
    xp[] = y2
    xp[] = (1 / m) * (u[1] - kv * x[3])
    xp[] = z2
    xp[] = (1 / m) * (u[2] - kv * x[5])
    return xp

# Runge Kutta order 4 ode solver
def rk4_mass(x, u, m, h):
    hsim = h # Integration step
    K1 = ode2(x, u, m)
    K2 = ode2(x + 0.5 * hsim * K1, u, m)
    K3 = ode2(x + 0.5 * hsim * K2, u, m)
    K4 = ode2(x + 1.0 * hsim * K3, u, m)
    
    x = x + (1 / 6) * hsim * (K1 + 2 * K2 + 2 * K3 + K4)
    return x

# 3D coordinate system visualization
def cord3D(b, R, screen):
    # b = [L, cn, a1, a2, a3, mlt]
    L = b[0, 0]
    cn = b[1, 0]
    a1 = b[2, 0]
    a2 = b[3, 0]
    a3 = b[4, 0]
    mlt = b[5, 0]
    dt = b[6, 0]
    G = b[7, 0]
    
    px = L * R[0 , 0]
    py = L * R[1 , 0]
    px2 = L * R[0 , 1]
    py2 = L * R[1 , 1]
    px3 = L * R[0 , 2]
    py3 = L * R[1 , 2]
    
    pygame.draw.aaline(screen, (255, 0, 0), [250, 250], [px + cn, py + cn])
    pygame.draw.aaline(screen, (0, 255, 0), [250, 250], [px2 + cn, py2 + cn])
    pygame.draw.aaline(screen, (0, 0, 255), [250, 250], [px3 + cn, py3 + cn])
    
    M = 2 * L
    
    px1 = cn
    py1 = cn
    px2 = M * R[0, 0] + cn
    py2 = M * R[1, 0] + cn
    px3 = M * R[0, 0] + M * R[0, 1] + cn
    py3 = M * R[1, 0] + M * R[1, 1] + cn
    px4 = M * R[0, 1] + cn
    py4 = M * R[1, 1] + cn
    px5 = M * R[0, 1] + M * R[0, 2] + cn
    py5 = M * R[1, 1] + M * R[1, 2] + cn
    px6 = M * R[0, 2] + cn
    py6 = M * R[1, 2] + cn
    px7 = M * R[0, 0] + M * R[0, 2] + cn
    py7 = M * R[1, 0] + M * R[1, 2] + cn
    px8 = M * R[0, 0] + M * R[0, 1] + M * R[0, 2] + cn
    py8 = M * R[1, 0] + M * R[1, 1] + M * R[1, 2] + cn
    
    # print(px1.shape, px2, px3, px4, px5, px6, px7, px8)
    # print(py1, py2, py3, py4, py5, py6, py7, py8)

    scralp = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp, (0, 0, 0, 30), [[px1, py1], [px2, py2], [px3, py3], [px4, py4]], 0)

    scralp2 = pygame.Surface((500, 500), pygame.SRCALPHA)    
    pygame.draw.polygon(scralp2, (0, 0, 0, 30), [[px1, py1], [px4, py4], [px5, py5], [px6, py6]], 0)
    
    scralp3 = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp3, (0, 0, 0, 30), [[px1, py1], [px2, py2], [px7, py7], [px6, py6]], 0)

    screen.blit(scralp, 0, 0)
    screen.blit(scralp2, 0, 0)
    screen.blit(scralp3, 0, 0)
    
# Mass 3D visualitation
def mass3D(b, R, x, color, r, screen):
    # b = [L, cn, a1, a2, a3, mlt]
    L = b[0, 0]
    cn = b[1, 0]
    a1 = b[2, 0]
    a2 = b[3, 0]
    a3 = b[4, 0]
    mlt = b[5, 0]
    dt = b[6, 0]
    G = b[7, 0]
    
    ppx = x[0, 0] * mlt # Posición en el eje x
    ppy = x[2, 0] * mlt # Posición en el eje y
    ppz = x[4, 0] * mlt # Posición en el eje z
    
    prx = ppx * R[0, 0] + ppy * R[0, 1] + ppz * R[0, 2] + cn
    pry = ppx * R[1, 0] + ppy * R[1, 1] + ppz * R[1, 2] + cn
    
    scralp = pygame.Surface((500, 500), pygame.SRCALPHA)
    # pygame.draw.circle(scralp, (10, 10, 255, 130), (prx, pry), 3)
    pygame.draw.circle(scralp, color, (prx, pry), r)
    screen.blit(scralp, (0, 0))
    
# Rotation keys
def rotkey(b, keys, screen):
    # b = [L, cn, a1, a2, a3, mlt]
    L = b[0, 0]
    cn = b[1, 0]
    a1 = b[2, 0]
    a2 = b[3, 0]
    a3 = b[4, 0]
    mlt = b[5, 0]
    dt = b[6, 0]
    G = b[7, 0]
    
    ic = 1
    
    if keys[pygame.K_q]:
        a1 += ic * dt
    if keys[pygame.K_a]:
        a1 -= ic * dt
    if keys[pygame.K_w]:
        a2 += ic * dt
    if keys[pygame.K_s]:
        a2 -= ic * dt
    if keys[pygame.K_e]:
        a3 += ic * dt
    if keys[pygame.K_d]:
        a3 -= ic * dt
    if keys[pygame.K_z]:
        mlt += ic * dt * 1
    if keys[pygame.K_x]:
        mlt -= ic * dt * 1
        
    if keys[pygame.K_r]:
        a1 = 0
        a2 = 0
        a3 = 0
        mlt = 5
        
    return a1, a2, a3, mlt

# Distance between planets
def dist2mass(X):
    z = X.shape
    n = z[1]
    
    d = np.zeros((n, n))
    # d12 = np.sqrt((x1[0] - x2[0]) ** 2 + (x1[2] - x2[2]) ** 2 + (x1[4] - x2[4]) ** 2)
    
    for k in range(n):
        for r in range(1 + k, n):
            # print(k, r)
            d[k, r] = np.sqrt((X[0, k] - X[0, r]) ** 2 + (X[2, k] - X[2, r]) ** 2 + (X[4, k] - X[4, r]) ** 2)
            d[r, k] = d[k, r]
            return d

# Unitary vector calculation
def uvect(X, d):
    z = X.shape
    n = z[1]
    
    u = np.zeros((n, n, 3))
    for k in range(n):
        for r in range(n):
                u[k, r, 0] = (X[0, k] - X[0, r]) / d[k, r]
                u[k, r, 1] = (X[2, k] - X[2, r]) / d[k, r]
                u[k, r, 2] = (X[4, k] - X[4, r]) / d[k, r]
                u[r, k, 0] = -u[k, r, 0]
                u[r, k, 1] = -u[k, r, 1]
                u[r, k, 2] = -u[k, r, 2]
    return u

# Calcular entrada
def incl(Un, D, radios, mv, n, rg, U, G, radius_proyectil):
    uv = np.zeros((n, 3))
    for k in range(n):
        for r in range (n-1):
            qx = k
            qy = (k + r + 1) % n
            for p in range(3):
                Pkp = Un[qx, qy, p] * D[qx, qy, p]
                
                vrkp = 2 * radios[k, 0] * Un[qx, qy, p]
                if qy == n - 1:
                    vrkp = radius_proyectil * Un[qx, qy, p]
                
                Fr = rg * (Pkp - vrkp) * (0.5 + 0.5 * np.sign(abs(vrkp) - abs(Pkp)))
                # if abs(Fr) > 0:
                    # print(Fr, Pkp, vrkp, p)
                    # running = False
                # Fr = rg * (Pkp - vrkp) * (0.5 + 0.5 * np.tanh(100 * (abs(vrkp) - abs(Pkp))))
                
                uv[k, p] = uv[k, p] - G * mv[qx, 0] * mv[qy, 0] * Un[qx, qy, p] * (1 / (D[qx, qy] ** 2)) - Fr
                
                # print("Eje: ", p, " Ppk: ", Ppk, " vrkp: ", vrkp, " Activar: " (0.5 + 0.5 * np.sign(vrkp - Pkp)))
            U[:, k] = uv[k, :]
        return U

# Runge Kutta order 4 ode solver 2
def rk4_mass2(x, u, m, h):
    hsim = h # Integration step
    K1 = ode2(x, u, m)
    K2 = ode2(x + 0.5 * hsim * K1, u, m)
    K3 = ode2(x + 0.5 * hsim * K2, u, m)
    K4 = ode2(x + 1.0 * hsim * K3, u, m)
    
    x = x + (1 / 6) * hsim * (K1 + 2 * K2 + 2 * K3 + K4)
    return x