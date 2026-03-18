import subprocess
import time

ip = "192.168.4.27"
tiempos = []

print(f"Iniciando monitoreo de {ip}...")

for i in range(5):  # Lo haremos 5 veces
    res = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
    
    if res.returncode == 0:
        # Extraemos el tiempo (usando tu lógica de la posición 6)
        linea_tiempo = res.stdout.splitlines()[1] # Tomamos la segunda línea del ping
        palabra_tiempo = linea_tiempo.split()[6]
        valor = float(palabra_tiempo.replace("time=", ""))
        
        tiempos.append(valor)
        print(f"Intento {i+1}: {valor} ms")
    
    time.sleep(1) # Esperamos 1 segundo antes del próximo

print(f"\nAnálisis final: El tiempo promedio fue {sum(tiempos)/len(tiempos):.3f} ms")
