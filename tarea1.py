#matriz busqueda en arreglo multidimencional
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Función para buscar un valor en la matriz
def buscar_en_matriz(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)
    return None

# Valor a buscar
valor_a_buscar = 7
posicion = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar resultado de la búsqueda
if posicion:
    print(f'Valor {valor_a_buscar} encontrado en la posición: {posicion}')
else:
    print(f'Valor {valor_a_buscar} no encontrado en la matriz.')