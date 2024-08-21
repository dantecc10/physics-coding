import numpy as np # Operaciones matemáticas
import pygame

# Inicialización de pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0

# Configuración para mostrar texto
my_font = pygame.font.SysFont('Arial',10)

class Vector:
    def __init__(self, origin, end, color=(30, 30, 30)):
        self.origin = list(origin)
        self.mg2ang = list(mg2ang)
    
    def draw(self, screen):
        rdf = 2
        punto_final_x = slef