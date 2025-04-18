import pandas as pd
from sqlalchemy import create_engine

# Crear conexión
engine = create_engine('postgresql://user:user1@localhost:5434/purchases_db')

# Leer tabla raw_data
df = pd.read_sql('SELECT * FROM raw_data', engine)

# Guardar como Parquet
df.to_parquet('../data/raw_data.parquet', index=False)

print("Extracción completada y archivo Parquet generado.")
