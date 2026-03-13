import subprocess
import sqlite3
import time

# 1. Configuración de la Base de Datos
conexion = sqlite3.connect("red.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS monitoreo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        latencia REAL
    )
""")
conexion.commit()

# 2. Lógica del Ping y Extracción de Datos
ip_objetivo = "192.168.4.27" # Tu IP

def registrar_ping():
    res = subprocess.run(["ping", "-c", "1", ip_objetivo], capture_output=True, text=True)
    
    if res.returncode == 0:
        # Extraemos el tiempo (Posición 6 después del split)
        linea_tiempo = res.stdout.splitlines()[1]
        palabra_tiempo = linea_tiempo.split()[6]
        valor_latencia = float(palabra_tiempo.replace("time=", ""))
        
        # 3. Guardado en Base de Datos
        cursor.execute("INSERT INTO monitoreo (ip, latencia) VALUES (?, ?)", (ip_objetivo, valor_latencia))
        conexion.commit()
        print(f"✅ Guardado: {valor_latencia} ms")
    else:
        print("❌ Error en el ping")

# Ejecutamos una prueba
registrar_ping()

# 4. Conteo de registros (Tu próximo paso)
# resultado = cursor.execute("SELECT ...").fetchone()[0]
