# Operación de convolución

n1 = 4
n2 = 2
W = [n1, n1]
C = [n2, n2]

W = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

C = [
    [1, 0],
    [0, -1]
]

def convolution(W, C):
    n11 = len(W)
    n12 = len(W[0])
    n21 = len(C)
    n22 = len(C[0])
    
    if n11 < n21 or n12 < n22:
        return 0
    
    n1 = n11 - n21 + 1
    n2 = n12 - n22 + 1
    result = []
    for i in range(n1):
        result.append([])
        for j in range(n2):
            result[i].append(0)
            for k in range(n21):
                for l in range(n22):
                    result[i][j] += W[i + k][j + l] * C[k][l]
    return result
    
C = (convolution(W, C))

print(C)