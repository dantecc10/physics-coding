import numpy as np

# Definición de las coordenadas de las masas
masas = [
    [1, 2],
    [3, 6],
    [7, 1],
    [5, 0],
    [7, 8]
]

def unit_vectors(distances_array):
    n = len(distances_array)
    uv = np.zeros((n, 2))

    for i in range (n):
        module = np.sqrt(np.power(distances_array[i][0], 2) + np.power(distances_array[i][1],2))
        unit_vector = [distances_array[i][0] / module, distances_array[i][1] / module]
        uv[i] = unit_vector
    return uv

# Función para calcular las distancias
def calculate_distances(distances_array):
    n = len(distances_array)
    
    # Inicializamos una matriz de ceros de tamaño n x n
    D = np.zeros((n, n))
    
    # Calculamos las distancias entre cada par de puntos
    for i in range(n):
        for j in range(i, n):  # Comenzamos en i para evitar recalcular distancias
            if i == j:
                D[i][j] = 0  # La distancia de un punto consigo mismo es 0
            else:
                # Calculamos la distancia euclidiana
                d = np.sqrt(np.power((distances_array[i][0] - distances_array[j][0]), 2) + np.power((distances_array[i][1] - distances_array[j][1]), 2))
                D[i][j] = d
                D[j][i] = d  # La distancia es simétrica
    
    return D

# Llamada a la función con el array de masas
distancias = calculate_distances(masas)

def show_data(distances):
    n = len(distances)
    for i in range(n):
        for j in range(n):
            print("la distancia de la masa ", (i + 1), " a la masa ", (j + 1), " es de ", distances[i,j], " u.")

print(distancias)
show_data(distancias)

print(unit_vectors(distancias))
