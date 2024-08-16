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
        magnitude = np.sqrt((self.end[0]-self.origin[0])**2+(self.end[1]-self.origin[1])**2)
        
        # Dibujar la flecha del vector
        triangle_points = [
            (self.arrow_size*np.cos(theta)+self.end[0], self.arrow_size*np.sin(theta)+self.end[1]),
            (self.arrow_size * np.cos(theta+(120*(np.pi/180))) + self.end[0],
            self.arrow_size * np.sin(theta+(120*(np.pi/180))) + self.end[1]),
            (self.arrow_size * np.cos(theta+(240*(np.pi/180))) + self.end[0],
            self.arrow_size * np.sin(theta+(240*(np.pi/180))) + self.end[1]),
        ]
        
        pygame.draw.polygon(screen, self.color, triangle_points)
        
        # Mostrar las propiedades del vector
        magnitude_text = my_font.render('Magnitud: ' + str(magnitude), False, (0, 0, 0))
        
        orientation_text = my_font.render('Orientación: ' + str(theta), False, (0, 0, 0))
        
        screen.blit(magnitude_text, (10, 0))
        
        screen.blit(orientation_text, (250, 0))
        
    # Método para mover el punto final del vector
    def move_end(self, dx, dy):
        self.end[0] += dx
        self.end[1] += dy
        
    # Método para mover el punto origen del vector
    def move_origin(self, dx, dy):
        self.origin[0] += dx
        self.origin[1] += dy
        
    def reset(self):
        self.origin = (0, 0)
        self.end = (0, 30)
    
# Crear un vector
vector = Vector(origin=(0, 0), end = (0, 30))