import requests
import pandas as pd
import json
import time

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

'''
base_datos = "torneos002"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
    print(f"Insertando {doc['Tournament']} | {response.status_code}")
    time.sleep(0.1)  # Esperar 100ms entre cada petición porque o si no se me cuelga el couchDB y se "resetea" la conexión.
'''

base_datos = "torneos003"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos por bloques
# Esto si lo saque de chatGPT porque se me pasa resentando la conexion :c
# Lo que hace es practicamnete enviar por bloques de mil los datos y esperar un segundo por cada bloque
for i in range(0, len(lista_datos), 1000):
    bloque = lista_datos[i:i+1000]
    for doc in bloque:
        try:
            response = requests.post(
                url,
                json=doc,
                headers=headers
            )
            print(f"Insertando {doc['Tournament']} | {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error insertando {doc['Tournament']}: {e}")
    print(f"--- Bloque {i//1000 + 1} enviado ---")
    time.sleep(0.1)  # Pausa de 1 segundo entre bloques