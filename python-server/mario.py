import pygame
import numpy as np

# Inicialización de Pygame
pygame.init()
t = 0
# Cargar imagen y convertirla para procesamiento
imagen = pygame.image.load('img1.jpg')
imagen = pygame.transform.scale(imagen, (300, 300))  # Escala la imagen a un tamaño manejable
pixels = pygame.surfarray.array3d(imagen)  # Obtiene los píxeles en una matriz 3D (RGB)

# Definir filtros convolucionales (kernels)
kernel_edge = np.array([[-1, 5, -10],  # Kernel para detección de bordes
                        [5, -5, 2],
                        [1, 2, 3]])

kernel_blur = np.array([[0, 0, 0],  # Kernel para desenfoque
                        [0, 0, 0],
                        [0, 0, 0]])

kernel_sharpen = np.array([[1, 1, 1],   # Kernel para realzar bordes
                           [1, 1, 1],
                           [1, 1, 1]])

# Aplicar convolución
def aplicar_filtro(pixels, kernel):
    alto, ancho, _ = pixels.shape
    resultado = np.zeros((alto, ancho, 3))  # Almacena el resultado de la convolución
    
    # Recorre cada píxel de la imagen (excluyendo bordes)
    for x in range(1, ancho - 1):
        for y in range(1, alto - 1):
            # Aplicar el kernel convolucional a cada canal (R, G, B)
            for canal in range(3):
                submatriz = pixels[y - 1:y + 2, x - 1:x + 2, canal]  # Toma una submatriz de 3x3 alrededor del píxel
                valor = np.sum(submatriz * kernel)  # Calcula la convolución para ese píxel
                resultado[y, x, canal] = min(max(valor, 0), 255)  # Limita el valor entre 0 y 255
    
    return resultado.astype(np.uint8)  # Retorna el resultado en formato uint8 para usar en Pygame

# Seleccionar el filtro a aplicar y procesar la imagen
pixels_filtrados = aplicar_filtro(pixels, kernel_edge)  # Puedes cambiar kernel_edge a otro kernel
imagen_filtrada = pygame.surfarray.make_surface(pixels_filtrados)  # Convierte la matriz de nuevo a una superficie

# Mostrar la imagen filtrada en pantalla
pantalla = pygame.display.set_mode((300, 300))
pantalla.blit(imagen_filtrada, (0, 0))
pygame.display.flip()

# Mantener la ventana abierta hasta que el usuario la cierre
running = True

while running:
    for event in pygame.event.get():
        rk = np.array([[np.sin(t * 7 ), np.cos(4 * t), np.sin(3 * t)], [np.sin(t * 7 ), np.cos(4 * t), np.sin(3 * t)], [np.sin(t * 7 ), np.cos(4 * t), np.sin(3 * t)]])
        pixels_filtrados = aplicar_filtro(pixels, rk)  # Puedes cambiar kernel_edge a otro kernel
        imagen_filtrada = pygame.surfarray.make_surface(pixels_filtrados)
        # Mostrar la imagen filtrada en pantalla
        pantalla = pygame.display.set_mode((300, 300))
        pantalla.blit(imagen_filtrada, (0, 0))
        pygame.display.flip()
        t += .5
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
