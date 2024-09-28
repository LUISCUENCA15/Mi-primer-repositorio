# Crear el diccionario 'informacion_personal'
informacion_personal = {
    "nombre": "Luis Cuenca",
    "edad": 34,
    "ciudad": "Arenillas",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado a "ciudad"
informacion_personal["ciudad"] = "Arenillas"

# Agregar una nueva clave-valor "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998141777"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
