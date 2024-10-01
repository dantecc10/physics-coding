import numpy as np
import pygame


# Definición de clases ---------------------------------- #
class Vector:
    '''Constructor -------------------------------------'''
    def __init__(self, origen, mg2ang,color):
        self.origen     = list(origen)
        self.mg2ang     = list(mg2ang)
        self.color      = list(color)
        '''self.magnitud   = magnitud
        self.angulo     = angulo'''
        
       
    '''Dibujar vector por medio de magnitud y ángulo ---'''
    def draw(self, screen):
        rdf = 4
        punto_final_x = self.origen[0] + self.mg2ang[0] * np.cos(self.mg2ang[1])
        punto_final_y = self.origen[1] + self.mg2ang[0] * np.sin(self.mg2ang[1])
        theta = self.mg2ang[1]
        
        pygame.draw.aaline(screen, self.color,
                           self.origen, (punto_final_x,punto_final_y), 1)

        triangle_points = [
            (rdf * np.cos(theta) + punto_final_x, rdf * np.sin(theta) + punto_final_y),
            (rdf * np.cos(theta + (120 * (np.pi / 180))) + punto_final_x,
             rdf * np.sin(theta + (120 * (np.pi / 180))) + punto_final_y),
            (rdf * np.cos(theta + (240 * (np.pi / 180))) + punto_final_x,
             rdf * np.sin(theta + (240 * (np.pi / 180))) + punto_final_y)
        ]

        pygame.draw.polygon(screen, self.color, triangle_points)

    def mod_angulo(self, ang):
        self.mg2ang[1] = ang
        
    def mod_magnitud(self, mgt):
        self.mg2ang[0] = mgt
    

    def ver_punt_extr(self):
        return list((self.origen[0] + self.mg2ang[0] * np.cos(self.mg2ang[1]),
                     self.origen[1] + self.mg2ang[0] * np.sin(self.mg2ang[1])))



# ------------------------------------------------------- #




def init_pygame():
    pygame.init()
    screen  = pygame.display.set_mode((500, 500))
    clock   = pygame.time.Clock()
    my_font = pygame.font.SysFont('Arial', 10)
    return screen, clock, my_font
