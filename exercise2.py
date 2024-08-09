# import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

x1 = 200
y1 = 70

x2 = x1 + 450
y2 = y1 + 450

x3 = x1 + 450
y3 = y1 + 150

x4 = x1 + 150
y4 = y1 + 450

while running: 
    # poll for events
    # pygame.QUIT event means the user clicked X on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("white")

    pygame.draw.aaline(screen, "red", [x1, y1], [x2, y2], 10)
    pygame.draw.aaline(screen, "red", [x2, y2], [x3, y3], 10)
    pygame.draw.aaline(screen, "red", [x2, y2], [x4, y4], 10)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y2 -= 300 * dt
    if keys[pygame.K_DOWN]:
        y2 += 300 * dt
    if keys[pygame.K_LEFT]:
        x2 -= 300 * dt
    if keys[pygame.K_RIGHT]:
        x2 += 300 * dt
        
    if keys[pygame.K_r]:
        x1 = 200
        y1 = 70
        
        x2 = x1 + 450
        y2 = y1 + 450
        
        x3 = x1 + 450
        y3 = y1 + 150
        
        x4 = x1 + 150
        y4 = y1 + 450
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
