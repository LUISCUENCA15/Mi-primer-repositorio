# Crear una matriz 3x3 con valores numéricos
matriz = [
    [5, 2, 7],
    [9, 5, 1],
    [3, 8, 4]
]

def buscar_valor(matriz, valor_a_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_a_buscar:
                return f"Valor {valor_a_buscar} encontrado en la posición ({i}, {j})"
    return f"Valor {valor_a_buscar} no encontrado en la matriz"

# Definir el valor a buscar
valor = 7

# Realizar la búsqueda
resultado = buscar_valor(matriz, valor)
print(resultado)
