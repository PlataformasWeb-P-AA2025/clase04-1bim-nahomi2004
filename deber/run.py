import requests
import pandas as pd

# Leer CSV con codificación compatible
df = pd.read_csv('atp_tennis.csv', encoding='latin1')

# Guardar como JSON
df.to_json('datos.json', orient='records', lines=True, force_ascii=False)