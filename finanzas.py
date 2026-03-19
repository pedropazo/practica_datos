import urllib.request
import json
import ssl
import sqlite3

# 1. Configurar Base de Datos (creará finanzas.db automáticamente)
conexion = sqlite3.connect("finanzas.db")
cursor = conexion.cursor()

# Creamos la tabla para el historial del precio
cursor.execute("""
    CREATE TABLE IF NOT EXISTS historial_btc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        precio REAL
    )
""")
conexion.commit()

# 2. Conexión a la API de Binance
contexto_seguridad = ssl._create_unverified_context()
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

print("⏳ Consultando el precio actual en Binance...")
respuesta = urllib.request.urlopen(url, context=contexto_seguridad)
datos = json.loads(respuesta.read())

# Convertimos el texto del precio a un número decimal (float)
precio_actual = float(datos['price'])

# 3. Guardar el precio en SQLite
# Nota: En Python, si envías un solo parámetro a SQL, debes poner una coma al final: (precio_actual,)
cursor.execute("INSERT INTO historial_btc (precio) VALUES (?)", (precio_actual,))
conexion.commit()

# 4. Verificar cuántos registros tenemos usando COUNT
total = cursor.execute("SELECT COUNT(*) FROM historial_btc").fetchone()[0]

print(f"✅ ¡Guardado exitoso! Precio de BTC: ${precio_actual}")
print(f"📊 Total de consultas guardadas en la base de datos: {total}")