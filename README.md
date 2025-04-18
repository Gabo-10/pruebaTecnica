# Prueba Técnica 

- Este proyecto contiene dos partes: una realcionada con procesamiento y transformación de datos usando PostgreSQL y Python, la otra relacionada con la creacion de una API para calcular el numero faltante.

# Sección 1: Procesamiento y Transferencia de Datos

## Objetivo:
Crear un proceso con las herramientas disponibles por el usuario.

### Herramientas utilizadas 
- Entonrno de desarrollo: Visual Studio Code
- Lenguaje: Python 3
- Base de datos: PostgresSQL
- Contenedores: Docker

## 1.1 Carga de información.
- Base de datos eligida : PosrgreSQL
- Motivo de mi Eleccion: PosrgreSQL es ideal para trabajar con datos estructurados y ofrecer soporte transaccional. La elección se baso en la necesidad de un motor de base de datos robusto para almacenar grandes volúmenes de informacion. Además PostgreSQL permite el uso de funciones avanzadas y es bien soportado en entornos de Docker, lo que facilita su integración con el proyecto.
### Retos encontrados
- Fue necesario ajustar algunos parámetros de conexión para poder acceder correctamente a la base de datos.

## 1.2 Extracción
- Lenguaje usado: Python
- Formato de extracción: CSV
- Motivo de mi eleción: Python es un lenguaje versatil muy utilizado para procesamiento de datos, y en esta caso se utilizó para extraer y transformar los datos del dataset propocionado. El formato CSV fue elegido debido a su simplicidad, compatibilidad y facilidad para ser procesado por bibliotecas como Pandas.
### Retos encontrados
- En esta parte fue manejar correctamente los valores nulos y los tipos de datos inconsistentes dentro del dataset original.

## 1.3 Transformación
- Se adaptaron los datos del dataset al esquema proporcionado, realizando ajustes a las columnas y tipos de datos.
- Se validaron los valores nulos y se aseguraron de que todas las columnas requeridas cumplieran con el formato esperado para  poder ser cargados  correctamente en la base de datos.
### Retos encontrados
- Hubo que mapear columnas que no coincidían directamente con los nombres del esquema propuesto.
- Algunos registros requerian un formato de fecha consistente, por lo que fue necesario hacer parsing manual de timestamps con distintos formatos.

## 1.4 Dispersión de la información
- Esquema de base de datos
- Tablas creadas: charges y companies
- Relación: Las tablas charges y companies estan relacionadas a través del campo company_id, lo que permite asociar las transacciones con las  compañias correspondientes.
### Retos encontrados
- Fue garantizar la integridad referencial al momento de insertar datos, asegurar que todas las charges tuvieran un company_id valido y ya existente en companies

## 1.5 SQL
- Vista creada: se diseño un vista en la base de datos que permite ver el monto total trasaccionado por dia para las diferentes compañias.

# Instalacion y ejecucion

#### 1: Usando Docker
- Terminal
    '''
    docker-compose up --build
    '''
#### 2: Manual´
1. Crear un entorno virtual:
- Terminal    
    '''
    python -m venv venv
    venv\Scripts\activate
    '''
2. Instalar las dependencias:
- Terminal
    '''
    pip install -r requirements.txt
    '''
3. Configurar base de datos PostgreSQL 

4. Ejecutar scripts en orden para cargar, transformar y dispersar la informacion

# Seccion 2: API para Número faltante 
### Ejecución

- Ejecutar desde terminal:

'''
uvicorn app.main:app --reload
'''

''' 
python -m app.main_cli (numero que desee)
'''
