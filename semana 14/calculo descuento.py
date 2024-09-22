# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal

# Primera llamada a la función (solo se proporciona el monto total, se aplica el descuento predeterminado del 10%)
monto_total_1 = 700
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Monto total: ${monto_total_1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")
print()

# Segunda llamada a la función (se proporciona el monto total y un porcentaje de descuento personalizado)
monto_total_2 = 1000
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(f"Monto total: ${monto_total_2}")
print(f"Descuento aplicado ({porcentaje_descuento_2}%): ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")
