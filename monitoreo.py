import subprocess
import sqlite3

# 1. Conexión a la base de datos
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

# 2. Ejecutar ping
ip_objetivo = "192.168.4.27"
res = subprocess.run(["ping", "-c", "1", ip_objetivo], capture_output=True, text=True)

if res.returncode == 0:
    # 3. Limpieza de datos (extraer el tiempo)
    linea_tiempo = res.stdout.splitlines()[1]
    palabra_tiempo = linea_tiempo.split()[6]
    valor_latencia = float(palabra_tiempo.replace("time=", ""))
    
    # 4. Insertar en la base de datos
    cursor.execute("INSERT INTO monitoreo (ip, latencia) VALUES (?, ?)", (ip_objetivo, valor_latencia))
    conexion.commit()
    
    # 5. Contar registros totales
    total = cursor.execute("SELECT COUNT(*) FROM monitoreo").fetchone()[0]
    print(f"✅ Guardado: {valor_latencia} ms. Total registros: {total}")