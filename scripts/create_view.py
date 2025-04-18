from sqlalchemy import create_engine, text

# Conexión
engine = create_engine('postgresql://user:user1@localhost:5434/purchases_db')

# Query para crear la vista
query = """
CREATE OR REPLACE VIEW daily_company_totals AS
SELECT
    company_id,
    company_name,
    DATE(created_at) AS transaction_date,
    SUM(amount) AS total_amount
FROM charges
GROUP BY company_id, company_name, DATE(created_at)
ORDER BY transaction_date, company_name;
"""

# Ejecutar el query para crear la vista
with engine.connect() as conn:
    conn.execute(text(query))
    print("Vista 'daily_company_totals' creada correctamente.")
