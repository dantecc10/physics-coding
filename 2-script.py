# import numpy as np
import pygame

'''
Tarea: Investigar qué es el Cálculo Diferencial (qué es la derivada)
'''

pygame.init()
screen = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
px = 50
py = 30

while running: 
    # poll for events
    # pygame.QUIT event means the user clicked X on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    pygame.draw.aaline(screen, (30, 30, 30), [0, 0], [px, py], 1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        py -= 300 * dt
    if keys[pygame.K_s]:
        py += 300 * dt
    if keys[pygame.K_a]:
        py -= 300 * dt
    if keys[pygame.K_d]:
        py += 300 * dt
    if keys[pygame.K_r]:
        px = 50
        py = 30
