import pandas as pd
from sqlalchemy import create_engine

# Conexión a PostgreSQL
engine = create_engine('postgresql://user:user1@localhost:5434/purchases_db')

# Cargar CSV
df = pd.read_csv('../data/data_prueba_tecnica.csv')

# Guardar en tabla raw_data
df.to_sql('raw_data', engine, if_exists='replace', index=False)

print("Carga completada.")
