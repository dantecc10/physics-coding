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
    px = L * R[0, 0]
    py = L * R[1, 0]
    
    px2 = L * R[0, 1]
    py2 = L * R[1, 1]
    
    px3 = L * R[0, 2]
    py3 = L * R[1, 2]
    
    pygame.draw.aaline(screen, (255, 0, 0), [250, 250], [px+250, py + 250], 1)
    pygame.draw.aaline(screen, (0, 255, 0), [250, 250], [px2+250, py2 + 250], 1)
    pygame.draw.aaline(screen, (0, 0, 255), [250, 250], [px3+250, py3 + 250], 1)
    # Dibujo del vector
    pygame.draw.aaline(screen, (30, 30, 30), [250, 250], [px + 50, px + 50], 1)
    
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
    
    
    keys = pygame.key.get_pressed()
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
    if keys[pygame.K_r]:
        a1 = 0
        a2 = 0
        a3 = 0
            
    txt4 = my_font.render('phi: ' + str(a1 * 57.29577951308232), False, (0, 0, 0))
    txt5 = my_font.render('theta: ' + str(a2 * 57.29577951308232), False, (0, 0, 0))
    txt6 = my_font.render('psi: ' + str(a3 * 57.29577951308232), False, (0, 0, 0))
    
    txt7 = my_font.render('FPS: ' + str(round(1 / dt)), False, (0, 0, 0))
    txt8 = my_font.render('FCC BUAP, Física I', False, (0, 0, 0))
            
            
    screen.blit(txt4, (10, 36))
    screen.blit(txt5, (10, 48))
    screen.blit(txt6, (10, 60))
    screen.blit(txt7, (460, 0))
    screen.blit(txt8, (10, 480))
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()
print('End of execution')

'''
import pygame
import numpy as np

# pygame setup
# Esto es un comentario

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Puntos para el vector
pcx = 0     # Punto Origen Vector
pcy = 0
px  = 0     # Punto Extremo Vector
py = 30

# Tamaño de la flecha
rdf = 5

# Configuración para mostrar texto
my_font = pygame.font.SysFont('Arial',10)

while running:

    # Esto sirve para que se cierre la ejecución cuando se cierra la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Esto sirve para rellenar la pantalla de color blanco
    screen.fill("white")



    # Aquí se dibuja el vector----------------------------------------------

    # Primero, se dibuja el segmento de recta, que toma el punto origen y el extremo
    pygame.draw.aaline(screen, (30, 30, 30), [pcx, pcy], [px, py], 1)
    
    # Se obtiene su orientación mediante el uso de la función trigonométrica arctan
    theta = np.arctan2(py-pcy,px-pcx)

    # Después se calcula la magnitud del vector
    mg1 = np.sqrt((px-pcx)**2+(py-pcy)**2)
    
    # La flecha se dibuja con un triángulo
    triangle_color = (0, 0, 0)
    triangle_points = [(rdf*np.cos(theta)+px,rdf*np.sin(theta)+py),(rdf*np.cos(theta+(120*(np.pi/180)))+px,rdf*np.sin(theta+(120*(np.pi/180)))+py),(rdf*np.cos(theta+(240*(np.pi/180)))+px,rdf*np.sin(theta+(240*(np.pi/180)))+py)]
    pygame.draw.polygon(screen, triangle_color, triangle_points)

    # Se muestran las propiedes asociadas al vector: magnitud y orientación
    txt1 = my_font.render('Magnitud: ' + str(mg1), False, (0,0,0))
    txt2 = my_font.render('Orientación: ' + str(theta), False, (0,0,0))
    screen.blit(txt1,(10,0))
    screen.blit(txt2,(250,0))
    #-----------------------------------------------------------------------


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

print('End of execution')

'''