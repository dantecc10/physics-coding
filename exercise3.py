import numpy as np
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

x0 = 500
y0 = 500

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
        theta -= 50# * dt
    if keys[pygame.K_DOWN]:
        theta += 5# * dt
    x1 = r * np.cos(theta) + x0
    y1 = r * np.sin(theta) + y0
    #if keys[pygame.K_LEFT]: x2 -= 300 * dt
    #if keys[pygame.K_RIGHT]: x2 += 300 * dt
        
    if keys[pygame.K_r]:
        x0 = 500
        y0 = 500

        # P1 = (r * cos(0) + x0, r * sin(0) + x0)
        theta = 100
        r = 200
        x1 = r * np.cos(theta) + x0
        y1 = r * np.sin(theta) + y0
        
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
