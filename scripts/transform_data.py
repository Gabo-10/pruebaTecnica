import pandas as pd

# Leer el Parquet original
df = pd.read_parquet('../data/raw_data.parquet')

# Renombrar columnas para que coincidan con el esquema requerido
df = df.rename(columns={
    'name': 'company_name',
    'paid_at': 'updated_at'
})

# Asegurar formatos y tipos
df['id'] = df['id'].astype(str)
df['company_id'] = df['company_id'].astype(str)
df['company_name'] = df['company_name'].astype(str)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').round(2)
df['status'] = df['status'].astype(str)
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')

# Guardar dataset transformado
df.to_parquet('../data/transformed_charges.parquet', index=False)

print("Transformación completada. Archivo generado: transformed_charges.parquet")
