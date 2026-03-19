import urllib.request
import json
import ssl  # 1. Importamos la librería de seguridad

# 2. Creamos un pase especial para ignorar el bloqueo de Mac
contexto_seguridad = ssl._create_unverified_context()

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# 3. Le pasamos el pase especial a urlopen
respuesta = urllib.request.urlopen(url, context=contexto_seguridad)

datos = json.loads(respuesta.read())

print(f"💰 El precio actual de Bitcoin es: ${datos['price']}")
