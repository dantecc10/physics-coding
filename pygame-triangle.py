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

    
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        py -= 300 * dt
    if keys[pygame.K_s]:
        py += 300 * dt
    if keys[pygame.K_a]:
        px -= 300 * dt
    if keys[pygame.K_d]:
        px += 300 * dt
        
    if keys[pygame.K_t]:
        pcy -= 300 * dt
    if keys[pygame.K_g]:
        pcy += 300 * dt
    if keys[pygame.K_f]:
        pcx -= 300 * dt
    if keys[pygame.K_h]:
        pcx += 300 * dt
        
    if keys[pygame.K_r]:
        px  = 0
        py  = 30
        pcx = 0
        pcy = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

print('End of execution')
