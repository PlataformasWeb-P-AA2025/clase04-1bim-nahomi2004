import requests
import pandas as pd
import json

# Esto funciona mas o menos, porque no convierte el csv a json con el formato adecuado
# Leer CSV con codificación compatible
# df = pd.read_csv('atp_tennis.csv', encoding='latin1')
# Guardar como JSON
#df.to_json('datos.json', orient='records', lines=True, force_ascii=False)

# Para eso mejor esta este codigo

# Leer el CSV
# La parte de encoding='latin1' sirve para que no te de un error por utf-8
df = pd.read_csv('atp_tennis.csv', encoding='latin1')

# Convertir a lista de diccionarios
datos = df.to_dict(orient='records')

# Crear la estructura final
estructura = {
    "docs": datos
}

# Guardar como JSON bonito y con acentos bien escritos
with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(estructura, f, ensure_ascii=False, indent=4)

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

base_datos = "torneos001"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta
print(response.status_code)
print(response.json())
