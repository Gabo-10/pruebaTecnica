import pandas as pd
from sqlalchemy import create_engine

# Conexión a PostgreSQL
engine = create_engine('postgresql://user:user1@localhost:5434/purchases_db')

# Leer el archivo transformado
df = pd.read_parquet('../data/transformed_charges.parquet')

# Crear tabla de compañías única
companies_df = df[['company_id', 'company_name']].drop_duplicates()
companies_df = companies_df.rename(columns={'company_id': 'id', 'company_name': 'name'})

# Cargar a la base de datos
companies_df.to_sql('companies', engine, if_exists='replace', index=False)
print("Tabla companies cargada.")

# Cargar datos en charges
df.to_sql('charges', engine, if_exists='replace', index=False)
print("Tabla charges cargada.")
