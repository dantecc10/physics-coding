import pygame
import numpy as np

# Inicialización de pygame
pygame.init()

# Definir la pantalla y el reloj
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

my_font = pygame.font.SysFont('Arial', 10)

class Masa:
    def __init__(self, position, mass, velocity=(0, 0), color=(0, 0, 255), radius=10):
        self.position = list(position)
        self.mass = mass
        self.velocity = list(velocity)
        self.color = color
        self.radius = radius

    def draw(self, screen):
        
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

    def move(self, dt):
        
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

    def apply_force(self, force, dt):
        
        acceleration = [force[0] / self.mass, force[1] / self.mass]
        self.velocity[0] += acceleration[0] * dt
        self.velocity[1] += acceleration[1] * dt

    def check_collision(self, other):
        
        distance = np.linalg.norm(np.array(self.position) - np.array(other.position))
        return distance <= self.radius + other.radius


def crear_masas(n_masas):
    
    masas = []
    for i in range(n_masas):
        position = (250, 100 + i * 50)  
        mass = 5
        velocity = (0, 0)
        color = (0, 0, 255) if i == 0 else (255, 0, 0)  
        radius = 10
        masas.append(Masa(position, mass, velocity, color, radius))
    return masas



masas = crear_masas(5)

force_value = 300  

running = True
while running:
    dt = clock.tick(60) / 1000  

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    
    for masa in masas:
        masa.move(dt)
        masa.draw(screen)

    
    keys = pygame.key.get_pressed()

    # Aplicar fuerzas a la primera masa
    if keys[pygame.K_w]:
        masas[0].apply_force((0, -force_value), dt)
    if keys[pygame.K_s]:
        masas[0].apply_force((0, force_value), dt)
    if keys[pygame.K_a]:
        masas[0].apply_force((-force_value, 0), dt)
    if keys[pygame.K_d]:
        masas[0].apply_force((force_value, 0), dt)

    # Verificar colisiones entre la primera masa y las demás
    for i in range(1, len(masas)):
        if masas[0].check_collision(masas[i]):
            # Empujar las demás masas hacia abajo si hay colisión
            masas[i].apply_force((0, force_value * 10), dt)  # Mayor fuerza hacia abajo

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar pygame
pygame.quit()
