# Definir dimensiones
num_ciudades = 3
num_semanas = 3
num_dias = 7

# Crear una lista 3D (ciudades, semanas, días) y llenarla con valores aleatorios entre 17 y 35 grados.
import random

# Nombres de las ciudades
ciudades = ["Ciudad de Arenillas", "Ciudad de Guayaquil", "Ciudad de Manta"]

# Crear la matriz 3D
temperaturas = [[[random.randint(17, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for ciudad in range(num_ciudades):
    print(f"\nPromedios de temperatura para {ciudades[ciudad]}:")
    for semana in range(num_semanas):
        promedio = sum(temperaturas[ciudad][semana]) / num_dias
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")

