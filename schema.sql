-- Crear tabla de companies
CREATE TABLE companies (
    id VARCHAR(24) PRIMARY KEY,
    name VARCHAR(130) NOT NULL
);

-- Crear tabla de charges
CREATE TABLE charges (
    id VARCHAR(24) PRIMARY KEY,
    company_name VARCHAR(130) NULL,
    company_id VARCHAR(24) NOT NULL,
    amount DECIMAL(16,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);
