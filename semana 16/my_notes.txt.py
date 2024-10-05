# Escritura de Archivo de Texto
# Abrimos (o creamos) un archivo llamado 'my_notes.txt' en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Primera nota personal.\n")
    file.write("Segunda nota personal.\n")
    file.write("Tercera nota personal.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos y mostramos el contenido línea por línea
    for line in file:
        print(line.strip())  # .strip() elimina los saltos de línea adicionales

# El archivo se cierra automáticamente al salir del bloque 'with'
