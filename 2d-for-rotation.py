import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 10)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

x0 = 500
y0 = 350

# P1 = (r * cos(0) + x0, r * sin(0) + x0)
theta = 40
r = 150
x1 = r * np.cos(theta) + x0
y1 = r * np.sin(theta) + y0

while running: 
    # poll for events
    # pygame.QUIT event means the user clicked X on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    pygame.draw.aaline(screen, "red", [x0, y0], [x1, y1], 10)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y1 -= 15# * dt
    if keys[pygame.K_DOWN]:
        y1 += 15# * dt
    if keys[pygame.K_LEFT]:
        x1 -= 15# * dt
    if keys[pygame.K_RIGHT]:
        x1 += 15# * dt
    #x1 = r * np.cos(theta) + x0
    #y1 = r * np.sin(theta) + y0
        
    if keys[pygame.K_r]:
        x0 = 500
        y0 = 350
        theta = 0
        r = 150
        x1 = r * np.cos(theta) + x0
        y1 = r * np.sin(theta) + y0
        
    # Textos con datos en tiempo real
    r = (np.sqrt(np.power((x1 - x0), 2) + np.power((y1 - y0), 2)))
    if r > 150:
        r = 150
        if x0 > x1:
            x1 = x0 - 150
        else:
            x1 = x0 + 150
    theta = np.arccos((x1 - x0) / r)
    txt5 = my_font.render('longitud: ' + str(r), False, (0, 0, 0))
    txt6 = my_font.render('theta: ' + str(theta), False, (0, 0, 0))
    txt7 = my_font.render('theta (grados): ' + str(theta * (180 / np.pi)), False, (0, 0, 0))
    txt8 = my_font.render('FCC BUAP, Física I', False, (0, 0, 0))
            
    screen.blit(txt5, (10, 48))
    screen.blit(txt6, (10, 60))
    screen.blit(txt7, (10, 72))
    screen.blit(txt8, (10, 480))
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
