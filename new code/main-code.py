import numpy as np
import pygame
import class_vector as v
import physics_tools as pt
import imageio

screen, clock, my_font = v.init_pygame()

# Constantes
G = 1e0 * 1
n = 2 # Masas
radius = 10
radius_proyectil = 10
#radius_proyectil = 1000
rg = 1e6
offr = 0

pygame.font.init()
font = pygame.font.Font(None, 20)

Masas = []

X = np.zeros((6, n)) # Posiciones masas
M = np.zeros((n, 1)) # Valor masas
U = np.zeros((3, n)) # Fuerzas
col_random_V = np.zeros((3, n))
radios = np.zeros((n, 1))

psrand_vec = np.zeros((3, n))
for k in range (n):
    col_random = np.random.uniform(0, 225, 3)
    pos_random = np.random.uniform(-100, 100, 3)
    #pos_random[2] = 0# The expression is K = 0.5 * np.sum(M * np.sum(X[1:4, :] ** 2, axis = 0))
    
    if k > n-2:
        Masas.append(pt.mass([0, -100, 0], [0, 200, 0], [0, 0, 0], 1e3))
        col_random_V[:, k] = np.reshape((0, 0, 0), (3,))
        radios[k] = radius_proyectil
        
    else:
        Masas.append(pt.mass(pos_random * 0 + [0, 10 + 30 * k, 0], [0, 0, 0], [0, 0, 0], 1e3))
        col_random_V[:, k] = np.reshape((255, 0, 0), (3,))
        radios[k] = radius
    
    aux = Masas[k].mkxp()
    X[:, k] = np.reshape(aux[0], (6,))
    M[k] = np.reshape(aux[1], (1,))
    U[:, k] = np.reshape(aux[2], (3,))

print(M)
L = 50
a1 = 0
a2 = 0
a3 = 0
mlt = 1
cn = 250

hsim = 1/60
dt = 1/60
running = True
b = np.zeros((8, 1)) # 

# Parámetros del video
video_frames = []
fps = 60 # Frames por segundo
filename = "simulacion7.mp4" # Nombre del archivo de video

while running:
    b[0] = L
    b[1] = cn
    b[2] = a1
    b[3] = a2
    b[4] = a3
    b[5] = mlt
    b[6] = dt
    b[7] = G
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    mv = M
    
    D = pt.dist2mass(X)
    Un = pt.uvect(X, D)
    U = pt.incl(Un, D, radios, mv, n, rg, U, G, radius_proyectil)
    
    # Método de Runge-Kutta
    K1 = np.zeros_like(X)
    for k in range(n):
        x = np.reshape(X[:, k], (6, 1))
        u = np.reshape(U[:, k], (3, 1))
        m = M[k]
        aux = pt.ode2(x, u, m)
        K1[:, k] = np.reshape(aux, (6,))
    
    K2, K3, K4 = np.zeros_like(X), np.zeros_like(X), np.zeros_like(X)
    for i, K, in enumerate([K2, K3, K4], start=1):
        for k in range(n):
            x = np.reshape(X[:, k] + (0.5 * i) * hsim * K1[:, k], (6, 1))
            u = np.reshape(U[:, k], (3, 1))
            m = M[k]
            aux = pt.ode2(x, u, m)
            K[:, k] = np.reshape(aux, (6,))
            
    X = X + (1/6) * hsim * (K1 + 2 * K2 + 2 * K3 + K4)
    
    a1 = a1 + 100
    a2 = a2 + 100
    a3 = a3 + 100
    
    R = pt.rot(a1, a2, a3)
    pt.cord3D(b, R, screen)
    
    for k in range(n):
        col_random = col_random_V[:, k]
        x = np.reshape(X[:, k], (6, 1))
        pt.mass3D(font,b, R, x, (col_random[0], col_random[1], col_random[2], 255), 10 + 0.0 * radios[k, 0] - offr, screen)
        
    keys = pygame.key.get_pressed()
    a1, a2, a3, mlt = pt.rotkey(b, keys, screen)
    #K_DISPLAY = (0.5 * np.sum(M * np.sum(X[1:4, :] ** 2, axis = 0)))
    #text1 = font.render("Energía Cinética (K) = " + K_DISPLAY.astype(str), True, (0, 0, 0))
    
    #n_length = len(Masas)
    #texts = [None] * n_length
    #for i in range(n_length):
    #    # dime como saco raíz cuadrad
    #    #v2 = np.sqrt(np.sum(Masas[i].v ** 2))
    #    v = np.sqrt(Masas[i].vel[0] ** 2 + Masas[i].vel[1] ** 2 + Masas[i].vel[2] ** 2)
    #    v2 = v ** 2
    #    m_displayable = (0.5 * Masas[i].m) * v2
    #    texts[i] = font.render("Masa " + str(i) + " = " + str(m_displayable), True, (0, 0, 0))
    #    screen.blit(texts[i], (50, 400 + 20 * i))
    # Imprimir el texto
    text1 = font.render('FPS: ' + str(dt), True, (0, 0, 0))
    screen.blit(text1, (50, 50))
    
    # Capturar el frame actual
    frame = pygame.surfarray.array3d(screen)
    frame = np.transpose(frame, (1, 0, 2)) # Transposición necesario para el formato correcto
    video_frames.append(frame)
    pygame.display.flip()
    
    dt = clock.tick(fps) / 1000
pygame.quit()
print("Fin de la simulación")

# Guardar el video
imageio.mimsave(filename, video_frames, fps=fps)
print("Video guardado en {filename}")
