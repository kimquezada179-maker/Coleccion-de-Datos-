# 1. Crear la colección de datos (diccionario)
estudiantes = {}

# 2. Agregar datos (nombre: nota en float)
estudiantes["Luis"] = 9.0
estudiantes["Paul"] = 8.0
estudiantes["Nora"] = 9.5

# 3. Recorrer y mostrar la información de forma clara
print("--- REGISTRO DE CALIFICACIONES ---")
for clave, valor in estudiantes.items():
    print(f"Estudiante: {clave} | Nota: {valor}")