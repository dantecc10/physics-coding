import numpy as np
import pygame

# nums = [2, 4, 5, 6] # Initial debugging array
masas = [
    [1, 2], # Masa 1, índice 0
    [3, 6], # Masa 2, índice 1
    [7, 1], # Masa 3, índice 2
    [5, 0], # Masa 4, índice 3
    [7, 8] # Masa 5, índice 4 
]

def unit_vectors(distances_array):
    n = len(distances_array)
    uv = np.zeros((n, 2))
    
    for i in range(n):
        module = np.sqrt(np.power(distances_array[i][0], 2) + np.power(distances_array[i][1], 2))
        unit_vector = [distances_array[i][0] / module, distances_array[i][1] / module]
        uv[i] = unit_vector
    return uv

def calculate_distances(distances_array):
    n = len(distances_array)
    D = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            if(i == j):
                D[i][j] = 0
            else:
                d = np.sqrt(np.power((distances_array[i][0] - distances_array[j][0]), 2)) + np.power((distances_array[i][1] - distances_array[j][1]), 2)
                D[i][j] = d
                D[j][i] = d
    return D

distancias = calculate_distances(masas)

def show_data(distances):
    n = len(distances)
    for i in range(n):
        for j in range(n):
            print("La distancia de la masa ", (i + 1), " a la masa ", (j + 1), " es de ", distances[i, j], " u.")
            
print(distancias)
show_data(distancias)

print(unit_vectors(distancias))