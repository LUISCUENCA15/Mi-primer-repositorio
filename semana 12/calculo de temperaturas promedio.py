import random

# Definir dimensiones
num_ciudades = 3
num_semanas = 3
num_dias = 7

# Nombres de las ciudades
ciudades = ["Ciudad de Arenillas", "Ciudad de Guayaquil", "Ciudad de Manta"]

# Crear una lista 3D (ciudades, semanas, días) y llenarla con valores aleatorios entre 16 y 35 grados.
temperaturas = [[[random.randint(16, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in
                range(num_ciudades)]


def calcular_promedio_ciudades(temperaturas, ciudades):
    """
    Función que calcula el promedio de temperatura para cada ciudad a lo largo de múltiples semanas.

    :param temperaturas: Lista 3D (ciudades, semanas, días) con las temperaturas diarias.
    :param ciudades: Lista de nombres de ciudades.
    :return: Diccionario con las ciudades y sus temperaturas promedio durante todo el período.
    """
    promedios_ciudad = {}

    # Iterar sobre cada ciudad
    for ciudad in range(len(temperaturas)):
        suma_total = 0
        contador_dias = 0

        # Calcular la suma total de temperaturas para cada ciudad
        for semana in range(len(temperaturas[ciudad])):
            suma_total += sum(temperaturas[ciudad][semana])
            contador_dias += len(temperaturas[ciudad][semana])

        # Calcular el promedio de la ciudad
        promedio_ciudad = suma_total / contador_dias
        promedios_ciudad[ciudades[ciudad]] = promedio_ciudad

    return promedios_ciudad


# Llamada a la función para calcular el promedio de temperaturas por ciudad
promedios = calcular_promedio_ciudades(temperaturas, ciudades)

# Mostrar los resultados
print("\nPromedio de temperaturas por ciudad durante 3 semanas:")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f} °C")
