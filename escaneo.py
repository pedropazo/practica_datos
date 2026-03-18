import subprocess

# Definimos la IP que queremos probar (puedes usar la de tu celular)
ip_objetivo = "192.168.4.27" 

# Ejecutamos el comando ping
# -c 1 indica que solo mande un paquete (en Mac/Linux)
resultado = subprocess.run(["ping", "-c", "1", ip_objetivo], capture_output=True, text=True)

# Revisamos si el comando tuvo éxito
if resultado.returncode == 0:
    print(f"✅ La IP {ip_objetivo} respondió correctamente.")
else:
    print(f"❌ No hubo respuesta de {ip_objetivo}.")

print("Este es el contenido de stdout:")
print(resultado.stdout)
