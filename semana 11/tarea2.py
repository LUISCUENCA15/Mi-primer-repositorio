#matriz ordenacion de arreglo multidimencional
matriz_ordenacion = [
    [9, 7, 3],
    [6, 5, 4],
    [1, 8, 2]
]
# Función de Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Ordenar la segunda fila (índice 1)
bubble_sort(matriz_ordenacion[1])

# Mostrar la matriz original y la matriz con la fila ordenada
print('Matriz original:')
for fila in matriz_ordenacion:
    print(fila)

print('Matriz con la fila ordenada:')
for fila in matriz_ordenacion:
    print(fila)