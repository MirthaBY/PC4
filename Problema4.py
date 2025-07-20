import requests
import sqlite3
import pymongo
from datetime import datetime, timedelta

# === 1. Función para obtener el tipo de cambio desde el API ===
def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "fecha": fecha,
            "compra": float(data["compra"]),
            "venta": float(data["venta"])
        }
    else:
        return None

# === 2. Función para guardar en SQLite ===
def guardar_sqlite(datos):
    conn = sqlite3.connect("base.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    """)
    for dato in datos:
        c.execute("INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)",
                  (dato["fecha"], dato["compra"], dato["venta"]))
    conn.commit()
    conn.close()

# === 3. Función para guardar en MongoDB ===
def guardar_mongodb(datos):
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")
    db = cliente["sunat"]
    coleccion = db["sunat_info"]
    for dato in datos:
        coleccion.update_one({"fecha": dato["fecha"]}, {"$set": dato}, upsert=True)

# === 4. Ejecutar para todas las fechas de 2023 ===
def main():
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    fecha_actual = fecha_inicio
    resultados = []

    while fecha_actual <= fecha_fin:
        fecha_str = fecha_actual.strftime("%Y-%m-%d")
        print(f"Consultando: {fecha_str}")
        resultado = obtener_tipo_cambio(fecha_str)
        if resultado:
            resultados.append(resultado)
        fecha_actual += timedelta(days=1)

    guardar_sqlite(resultados)
    guardar_mongodb(resultados)
    print("Datos guardados correctamente en SQLite y MongoDB.")

if __name__ == "__main__":
    main()
