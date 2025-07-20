import csv
import sqlite3
from pymongo import MongoClient
from collections import defaultdict
from datetime import datetime

# Conexión a SQLite
sqlite_conn = sqlite3.connect("base.db")
sqlite_cursor = sqlite_conn.cursor()

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["mi_base"]
ventas_collection = mongo_db["ventas_solarizadas"]

# 1. Leer CSV
ventas_usd = []
with open("ventas.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ventas_usd.append({
            "fecha": row["fecha"],
            "producto": row["producto"],
            "cantidad": float(row["cantidad"]),
            "precio_unitario_usd": float(row["precio_unitario_usd"])
        })

# 2. Leer tipo de cambio desde SQLite
sqlite_cursor.execute("SELECT fecha, venta FROM sunat_info")
tipo_cambio_dict = {row[0]: row[1] for row in sqlite_cursor.fetchall()}

# 3. Solarizar ventas
ventas_solarizadas = []
for venta in ventas_usd:
    fecha = venta["fecha"]
    tipo_cambio = tipo_cambio_dict.get(fecha)
    
    if tipo_cambio:
        total_soles = venta["cantidad"] * venta["precio_unitario_usd"] * tipo_cambio
        ventas_solarizadas.append({
            "producto": venta["producto"],
            "total_soles": total_soles
        })
    else:
        print(f"[!] No se encontró tipo de cambio para la fecha {fecha}")

# 4. Agrupar por producto
resumen = defaultdict(float)
for item in ventas_solarizadas:
    resumen[item["producto"]] += item["total_soles"]

# 5. Almacenar en MongoDB
resultado = [{"producto": k, "total_vendido_soles": round(v, 2)} for k, v in resumen.items()]
ventas_collection.insert_many(resultado)

print("✅ Datos solarizados y almacenados correctamente en MongoDB.")
