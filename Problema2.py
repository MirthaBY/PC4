

def crear_tabla_multiplicar():
    n = int(input("Introduce un número entero entre 1 y 10: "))
    if n < 1 or n > 10:
        print("Número fuera de rango.")
        return
    nombre_fichero = f"tabla-{n}.txt"
    with open(nombre_fichero, "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_fichero}.")

def mostrar_tabla():
    n = int(input("Introduce un número entero entre 1 y 10 para leer su tabla: "))
    nombre_fichero = f"tabla-{n}.txt"
    if not os.path.exists(nombre_fichero):
        print(f"El fichero {nombre_fichero} no existe.")
        return
    with open(nombre_fichero, "r") as f:
        contenido = f.read()
        print(f"Contenido de {nombre_fichero}:\n{contenido}")

def mostrar_linea_tabla():
    n = int(input("Introduce el número de la tabla (1-10): "))
    m = int(input("Introduce el número de línea a mostrar (1-10): "))
    nombre_fichero = f"tabla-{n}.txt"
    if not os.path.exists(nombre_fichero):
        print(f"El fichero {nombre_fichero} no existe.")
        return
    with open(nombre_fichero, "r") as f:
        lineas = f.readlines()
        if 1 <= m <= len(lineas):
            print(f"Línea {m}: {lineas[m-1].strip()}")
        else:
            print("Número de línea fuera de rango.")

# Menú para ejecutar las opciones
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear tabla de multiplicar")
        print("2. Mostrar tabla completa")
        print("3. Mostrar una línea específica de la tabla")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            crear_tabla_multiplicar()
        elif opcion == "2":
            mostrar_tabla()
        elif opcion == "3":
            mostrar_linea_tabla()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

menu()
