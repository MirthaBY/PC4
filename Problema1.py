def proceso_temperatura(fichero_entrada, fichero_salida):
    temperaturas = []

    try:
        with open(fichero_entrada, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    fecha, temp = linea.split(',')
                    temperaturas.append(float(temp))

        if temperaturas:
            temp_promedio = sum(temperaturas) / len(temperaturas)
            temp_maxima = max(temperaturas)
            temp_minima = min(temperaturas)

            with open(fichero_salida, 'w') as resumen:
                resumen.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")
                resumen.write(f"Temperatura máxima: {temp_maxima:.2f}°C\n")
                resumen.write(f"Temperatura mínima: {temp_minima:.2f}°C\n")
        else:
            print("No se encontraron datos de temperatura.")

    except FileNotFoundError:
        print(f"El fichero '{fichero_entrada}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la función
procesar_temperaturas('temperaturas.txt', 'resumen_temperaturas.txt')
