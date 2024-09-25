import pygame
import numpy as np

# Inicialización de pygame
pygame.init()

# Definir la pantalla y el reloj
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Fuente para mostrar texto
my_font = pygame.font.SysFont('Arial', 10)


class Masa:
    def __init__(self, position, mass, velocity=(0, 0), color=(0, 0, 255), radius=3):
        self.position = list(position)
        self.mass = mass
        self.velocity = list(velocity)
        self.color = color
        self.radius = radius

    def draw(self, screen):
        # Dibujar la masa como un círculo
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

        # Mostrar las propiedades de la masa
        mass_text = my_font.render(f'Masa: {self.mass:.2f}', False, (0, 0, 0))
        velocity_text = my_font.render(f'Velocidad: ({self.velocity[0]:.2f}, {self.velocity[1]:.2f})', False, (0, 0, 0))

        # Posicionar el texto en la pantalla
        screen.blit(mass_text, (10, 10))
        screen.blit(velocity_text, (10, 40))

    def move(self, dt):
        # Mover la masa según su velocidad
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

    def apply_force(self, force, dt):
        # Se aplica una fuerza (F = m * a) para cambiar la velocidad
        acceleration = [force[0] / self.mass, force[1] / self.mass]
        self.velocity[0] += acceleration[0] * dt
        self.velocity[1] += acceleration[1] * dt

    def reset(self):
        # Resetear la posición y la velocidad
        self.position = [250, 250]
        self.velocity = [0, 0]


# Definir la funcion de la Masa clase
masa = Masa(position=(250, 250), mass=5)

# Fuerza que se aplicará cuando se presionen las teclas
force_value = 300  

# Bucle principal del programa
running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time para el movimiento

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Dibujar la masa
    masa.draw(screen)

    # Obtener el estado de las teclas presionadas
    keys = pygame.key.get_pressed()

    # Aplicar fuerzas en función de las teclas presionadas
    if keys[pygame.K_w]:
        masa.apply_force((0, -force_value), dt)
    if keys[pygame.K_s]:
        masa.apply_force((0, force_value), dt)
    if keys[pygame.K_a]:
        masa.apply_force((-force_value, 0), dt)
    if keys[pygame.K_d]:
        masa.apply_force((force_value, 0), dt)

    # Resetear la posición de la masa
    if keys[pygame.K_r]:
        masa.reset()

    # Mover la masa
    masa.move(dt)

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar pygame
pygame.quit()
