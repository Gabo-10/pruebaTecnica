-- Muestra el total transaccionado por compañía y por día

CREATE OR REPLACE VIEW daily_company_totals AS
SELECT
    company_id,
    company_name,
    DATE(created_at) AS transaction_date,
    SUM(amount) AS total_amount
FROM charges
GROUP BY company_id, company_name, DATE(created_at)
ORDER BY transaction_date, company_name;
