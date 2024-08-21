# Campo vectorial 1, Física 1, FCC BUAP

# Librerías
import numpy as np
import pygame

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0
my_font = pygame.font.SysFont('Arial', 10)

# Definición de clases
class Vector:
    '''Constructor'''
    def init(self, origen, mg2ang):
        self.origen = list(origen)
        self.m2ang = list(mg2ang)
        '''self.magnitud = magnitud
        self.angulo = angulo'''
        
    '''Dibujar vector por medio de magnitud y ángulo'''
    def draw(self, screen):
        rdf = 2
        punto_final_x = self.origen[0] + self.mg2ang[0] * np.cos(self.mg2ang[1])
        punto_final_y = self.origen[1] + self.mg2ang[0] * np.sin(self.mg2ang[1])
        theta = self.mg2ang[1]
        
        pygame.draw.aaline(screen, (30, 30, 30), self.origen, (punto_final_x, punto_final_y), 1)
        
        triangle_points = [
            (rdf * np.cos(theta) + punto_final_x, rdf * np.sin(theta) + punto_final_y),
            (rdf * np.cos(theta + (120 * (np.pi / 180))) + punto_final_x,
             rdf * np.sin(theta + (120 * (np.pi / 180))) + punto_final_y),
            (rdf * np.cos(theta + (240 * (np.pi / 180))) + punto_final_x,
             rdf * np.sin(theta + (240 * (np.pi / 180))) + punto_final_y)        
        ]
        
        pygame.draw.polygon(screen, (30, 30, 30), triangle_points)
    
    def mod_angulo(self, ang):
        self.mg2ang[1] = ang
        
    def mod_angulo(self, mgt):
        self.mg2ang[1] = mgt
        
# Creación de vectores
n_row = 25
n_col = 25
esp_x = 20
esp_y = 20
mgt_v = 20
vectores = []

for i in range (n_row):
    for j in range (n_col):
        ox = j * esp_x
        oy = i * esp_y
        
        vector = Vector(origen = (ox,oy),
                        mg2ang = (mgt_v,0))
        vectores.append(vector)
        
# Variables globales
t = 0
m = 5
o = np.zeros((2, 1))


# Ciclo while principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        t += dt
        for vector in vectores:
            vector.mod_magnitud(mgt_v)
            vector.mod_angulo(np.sin(t * m) * 1)
            
    if keys[pygame.K_d]:
        t += dt
        for vector in vectores:
            o = vector.origen
            vector.mod_magnitud(mgt_v)
            vector.mod_angulo(np.sin(t * m) * o[0] * 0.01 + o[1] * 0.01)
    
    if keys[pygame.K_w]:
        t += dt
        for vector in vectores:
            o = vector.origen
            vector.mod_angulo(np.sin(t * m) * o[0] * 0.05 + np.cos(o[1] * 0.01))
            vector.mod_magnitud(0.4 * mgt_v + np.sin(t * 1) * 0.2 * mgt_v)
            
    if keys[pygame.K_s]:
        t += dt
        for vector in vectores:
            o = vector.origen
            vector.mod_magnitud(np.abs(mgt_v + np.sin(t * m * 2) * 0.5 + 0.5 * mgt_v) + o[0] * 0.2)
            vector.mod_angulo(t * m * 0.02 * mgt_v * 2 + o[1] * 0.01 * 0.02 * mgt_v + o[0] * 0.01 * 0.02 * mgt_v)
            
        
    for vector in vectores:
        vector.draw(screen)
        
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Limitar los FPS (Frames Per Second) a 60
    dt = clock.tick(60) / 1000
    
    # running = False
    
pygame.quit()

print("End of execution")