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

class Vector:
    # def es para definir una función
    # __init__ es el constructor
    def __init__(self, origin, end, color = (30, 30, 30), arrow_size = 5):
        self.origin = list(origin) # Punto origen
        self.end = list(end) # Punto final
        self.color = color
        self.arrow_size = arrow_size
        #print(self.end)
        
    #Este es un método para dibujar
    def draw(self, screen):
        # Dibujar la línea del vector
        # print(self.origin)
        pygame.draw.aaline(screen, self.color, self.origin, self.end, 1)
        
        # Calcular la orientación y magnitud del vector
        theta = np.arctan2(self.end[1]-self.origin[1],self.end[0]-self.origin[0])