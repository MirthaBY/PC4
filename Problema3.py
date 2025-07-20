

def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith(".py") or not os.path.isfile(ruta_archivo):
        return None

    lineas_codigo = 0
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            # Verifica que la línea no esté vacía ni sea un comentario
            if linea_limpia and not linea_limpia.startswith("#"):
                lineas_codigo += 1

    return lineas_codigo

def main():
    ruta = input("Ingrese la ruta del archivo .py: ").strip()
    resultado = contar_lineas_codigo(ruta)

    if resultado is not None:
        print(f"Cantidad de líneas de código (excluyendo comentarios y líneas en blanco): {resultado}")

if __name__ == "__main__":
    main()
