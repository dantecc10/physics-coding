import pygame
import numpy as np # Operaciones matemáticas

# Inicialización de pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0

# Configuración para mostrar texto
my_font = pygame.font.SysFont('Arial',10)

class Masa:
    def __init__(self, position, velocity, mass, color = (30, 30, 30), radius = 5):
        self.position = list(position)
        self.velocity = list(velocity)
        self.mass = mass
        self.color = color
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        
        # Mostrar las propiedades de la masa
        mass_text = my_font.render('Masa: ' + str(self.mass), False, (0, 0, 0))
        
        velocity_text = my_font.render('Velocidad: ' + str(self.velocity), False, (0, 0, 0))
        
        screen.blit(mass_text, (10, 0))
        
        screen.blit(velocity_text, (250, 0))
        
    def move(self, dx, dy):
        self.position[0] += dx
        self.position[1] += dy
        
    def apply_force(self, force):
        self.velocity[0] += force[0] / self.mass
        self.velocity[1] += force[1] / self.mass
    
    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
    
masa1 = Masa([100, 100], [1, 0], 1e3)
masa2 = Masa([400, 400], [1, 0], 1e3)

while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    masa1.draw(screen)
    masa2.draw(screen)
    masa1.update()
    masa2.update()
    masa1.apply_force([-3, 1])
    
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
