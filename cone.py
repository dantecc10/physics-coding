import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del cono
x_v, y_v, z_v = 0, 0, 5  # Vértice del cono
r = 2  # Radio de la base
h = 7  # Altura del cono

# Coordenadas del centro de la base
x_c, y_c, z_c = x_v, y_v, z_v - h

# Generar puntos de la base
theta = np.linspace(0, 2 * np.pi, 500)
x_base = x_c + r * np.cos(theta)
y_base = y_c + r * np.sin(theta)
z_base = np.full_like(theta, z_c)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar la base del cono
ax.plot(x_base, y_base, z_base, color='b')

# Dibujar líneas del vértice a los puntos de la base
for xb, yb, zb in zip(x_base, y_base, z_base):
    ax.plot([x_v, xb], [y_v, yb], [z_v, zb], color='r')

# Dibujar el vértice
ax.scatter([x_v], [y_v], [z_v], color='k')

# Configurar los límites y mostrar el gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
