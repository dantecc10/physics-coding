# Ejemplo de rotación en 3D

# Librerías
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 10)
clock = pygame.time.Clock()
running = True
dt = 1

# Variables globales 1
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
L = 50
a1 = 0
a2 = 0
a3 = 0
cont = 0
ic = 1

# Vector que quieres dibujar desde el origen
vector = np.array([30, 30, 30])

# Funciones
def rot(phi, tht, psi):
    # Esta función es para rotar objetos en 3D
    A = np.zeros((3, 3))
    
    A[0, 0] = np.cos(psi) * np.cos(tht)
    A[0, 1] = np.cos(psi) * np.sin(tht) * np.sin(phi) - np.sin(psi) * np.cos(phi)
    A[0, 2] = np.cos(psi) * np.sin(tht) * np.cos(phi) + np.sin(phi) * np.sin(psi)
    
    A[1, 0] = np.sin(psi) * np.cos(tht)
    #A[1, 1] = np.cos(psi) * np.sin(tht) * np.sin(phi) - np.sin(phi) * np.cos(psi) * np.cos(phi)
    A[1, 1] = np.sin(psi) * np.sin(tht) * np.sin(phi) + np.cos(phi) * np.cos(psi)
    A[1, 2] = np.sin(psi) * np.sin(tht) * np.cos(phi) - np.sin(phi) * np.cos(psi)
    
    
    A[2, 0] = -np.sin(tht)
    A[2, 1] = np.cos(tht) * np.sin(phi)
    A[2, 2] = np.cos(tht) * np.cos(phi)
    return A


while running:
    # Poll for events
    # pygame.QUIT event means that the user clicked the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # FIll the screen with white
    screen.fill((255, 255, 255))
    
    # Matriz de rotación
    R = rot(a1, a2, a3)
    
    # Marco de referencia
    px1 = L * R[0, 0]
    py1 = L * R[1, 0]
    
    px2 = L * R[0, 1]
    py2 = L * R[1, 1]
    
    px3 = L * R[0, 2]
    py3 = L * R[1, 2]
    
    pygame.draw.aaline(screen, (255, 0, 0), [250, 250], [px1 + 250, py1 + 250], 1)
    pygame.draw.aaline(screen, (0, 255, 0), [250, 250], [px2 + 250, py2 + 250], 1)
    pygame.draw.aaline(screen, (0, 0, 255), [250, 250], [px3 + 250, py3 + 250], 1)
    
    # Crear paredes con polígonos
    M = 2 * L
    cn = 250
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
    
    px8 = M * R[0, 0] + R[0, 1] + M * R[0, 2] + cn
    py8 = M * R[1, 0] + R[1, 1] + M * R[1, 2] + cn
    
    
    scralp = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp, (0, 0, 0, 30), [[px1, py1], [px2, py2], [px3, py3], [px4, py4]], 0)
    
    scralp2 = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp2, (0, 0, 0, 30), [[px1, py1], [px4, py4], [px5, py5], [px6, py6]], 0)
    
    scralp3 = pygame.Surface((500, 500), pygame.SRCALPHA)
    pygame.draw.polygon(scralp3, (0, 0, 0, 30), [[px1, py1], [px2, py2], [px7, py7], [px6, py6]], 0)
    
    screen.blit(scralp, (0, 0))
    screen.blit(scralp2, (0, 0))
    screen.blit(scralp3, (0, 0))
    
    # Rotación del vector
    vector_rotado = np.dot(R, vector)

    # Coordenadas proyectadas para el vector en la pantalla 2D
    px_vector = vector_rotado[0] + 250
    py_vector = vector_rotado[1] + 250
    
    # Dibuja el vector desde el origen (250, 250) hasta el punto rotado
    pygame.draw.aaline(screen, (0, 0, 0), [250, 250], [px_vector, py_vector], 1)
    
    txt1 = my_font.render('', False, (0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        a1 += ic * dt
    if keys[pygame.K_a]:
        a1 -= ic * dt
    if keys[pygame.K_w]:
        a2 += ic * dt
    if keys[pygame.K_s]:
        a2 -= ic * dt
    if keys[pygame.K_q]:
        a3 += ic * dt
    if keys[pygame.K_e]:
        a3 -= ic * dt
        
    if keys[pygame.K_UP]:
        vector[1] += ic * dt
    if keys[pygame.K_DOWN]:
        vector[1] -= ic * dt
    if keys[pygame.K_LEFT]:
        vector[0] -= ic * dt
    if keys[pygame.K_RIGHT]:
        vector[0] += ic * dt    
        
    if keys[pygame.K_LCTRL] and keys[pygame.K_x] and keys[pygame.K_PLUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "x" + "+"', False, (0, 0, 0))
        vector[0] += ic * dt
    if keys[pygame.K_LCTRL] and keys[pygame.K_x] and keys[pygame.K_MINUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "x" + "-"', False, (0, 0, 0))
        vector[0] -= ic * dt
    if keys[pygame.K_LCTRL] and keys[pygame.K_y] and keys[pygame.K_PLUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "y" + "+"', False, (0, 0, 0))
        vector[1] += ic * dt
    if keys[pygame.K_LCTRL] and keys[pygame.K_y] and keys[pygame.K_MINUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "y" + "-"', False, (0, 0, 0))
        vector[1] -= ic * dt
    if keys[pygame.K_LCTRL] and keys[pygame.K_z] and keys[pygame.K_PLUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "z" + "+"', False, (0, 0, 0))
        vector[2] += ic * dt
    if keys[pygame.K_LCTRL] and keys[pygame.K_z] and keys[pygame.K_MINUS]:
        txt1 = my_font.render('Pulsando: "Ctrl" + "z" + "-"', False, (0, 0, 0))
        vector[2] -= ic * dt
        
    if keys[pygame.K_r]:
        a1 = 0
        a2 = 0
        a3 = 0
        vector = np.array([30, 30, 30])
        
        
    # Textos con datos en tiempo real
    txt4 = my_font.render('phi (eje): ' + str(a1*57.29577951308232), False, (0, 0, 0))
    txt5 = my_font.render('theta (eje): ' + str(a2*57.29577951308232), False, (0, 0, 0))
    txt6 = my_font.render('psi (eje): ' + str(a3*57.29577951308232), False, (0, 0, 0))
    txt7 = my_font.render('FPS: ' + str(round(1 / dt)), False, (0, 0, 0))
    txt8 = my_font.render('FCC BUAP, Física I', False, (0, 0, 0))
    txt9 = my_font.render('Vector: (' + str(vector[0]) + ', ' + str(vector[1]) + ', ' + str(vector[2]) + ')', False, ('green'))
    txt10 = my_font.render('Magnitud del vector: ' + str(np.sqrt(np.power(vector[0], 2) + np.power(vector[1], 2) + np.power(vector[0], 2))), False, ('orange'))
    txt11 = my_font.render('Dante Castelán Carpinteyro', False, (0, 0, 0))
    txt12 = my_font.render('Ingeniería en Ciencias de la Computación', False, (0, 0, 0))
            
    screen.blit(txt1, (10, 24))
    screen.blit(txt4, (10, 36))
    screen.blit(txt5, (10, 48))
    screen.blit(txt6, (10, 60))
    screen.blit(txt7, (460, 10))
    screen.blit(txt8, (10, 456))
    screen.blit(txt11, (10, 432))
    screen.blit(txt12, (10, 444))
    screen.blit(txt9, (10, 72))
    screen.blit(txt10, (10, 84))
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()
print('End of execution')