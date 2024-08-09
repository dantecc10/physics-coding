# import numpy as np
import pygame

'''
Tarea: Investigar qué es el Cálculo Diferencial (qué es la derivada)
'''

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
x1 = 200
y1 = 70
y2 = y1
x2 = x1 + 500
x3 = x2
y3 = y2 + 100
x4 = x1
y4 = y1 + 100

while running: 
    # poll for events
    # pygame.QUIT event means the user clicked X on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    pygame.draw.aaline(screen, "red", [x1, y1], [x2, y2], 5)
    pygame.draw.aaline(screen, "blue", [x2, y2], [x3, y3], 5)
    pygame.draw.aaline(screen, "red", [x3, y3], [x4, y4], 5)
    pygame.draw.aaline(screen, "blue", [x4, y4], [x1, y1], 5)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y1 -= 300 * dt
        y4 -= 300 * dt
    if keys[pygame.K_s]:
        y1 += 300 * dt
        y4 += 300 * dt
    if keys[pygame.K_UP]:
        y2 -= 300 * dt
        y3 -= 300 * dt
    if keys[pygame.K_DOWN]:
        y2 += 300 * dt
        y3 += 300 * dt
        
    if keys[pygame.K_r]:
        x1 = 200
        y1 = 70
        y2 = y1
        x2 = x1 + 500
        x3 = x2
        y3 = y2 + 100
        x4 = x1
        y4 = y1 + 100
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
