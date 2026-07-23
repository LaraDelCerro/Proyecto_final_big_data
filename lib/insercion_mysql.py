import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv(override=True)



### Inserción de datos en MySQL ### 

#nos conectamos a mySQL
def get_connection():
    """
    Establece una conexión con la base de datos MySQL utilizando la
    configuración definida en DB_CONFIG.

    Retorna:
    mysql.connector.connection.MySQLConnection: Objeto de conexión con la
    base de datos si la conexión se establece correctamente.
    None: Si ocurre un error durante la conexión.
    """
    try:
        return mysql.connector.connect(**DB_CONFIG)
        #con ** pasamos como param a la fcón los valores del diccionario
        #es una desestructuración del diccionario, pasa de 1 vble(el dicc) a 5 vbles
    except Error as e:
        print(f'Error: {e}')
        return None


#INFO DB para conectar con mySQL
'''
DB_CONFIG = {
    'host' : os.getenv('MYSQL_HOST'),
    'port' : 3306,
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}
'''

# INFO DB para volcar los datos a Aiven (online)
DB_CONFIG = {
    'host' : os.getenv('MYSQL_HOST_A'),
    'port' : os.getenv('MYSQL_PORT_A'),
    'user': os.getenv('MYSQL_USER_A'),
    'password': os.getenv('MYSQL_PASSWORD_A'),
    'database': os.getenv('MYSQL_DATABASE_A')
}



def vaciar_tabla():
    """
    Elimina todos los registros de la tabla 'dataset_fao'.

    Retorna:
    None: Vacía la tabla y confirma los cambios en la base de datos.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dataset_fao")  # Elimina todos los registros de la tabla
        conn.commit()  # Confirma los cambios en la base de datos
        print("Tabla vaciada correctamente.")
    except Error as e:
        print(f'Error al vaciar la tabla: {e}')
    finally:
        conn.close()  # Cierra la conexión a la base de datos


def insert_emissions(df):
    """
    Inserta los datos de un DataFrame en la tabla 'dataset_fao' de la
    base de datos MySQL.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos de emisiones a
    insertar.

    Retorna:
    None: Inserta los registros en la base de datos y confirma los
    cambios si la operación se realiza correctamente.
    """
    sql = """INSERT INTO dataset_fao(
                codigo_area, area,
                codigo_elemento, elemento,
                codigo_producto, producto,
                anio, unidad, valor,
                simbolo, descripcion_simbolo)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    columnas = ['codigo_area', 'area', 'codigo_elemento', 'elemento',
                'codigo_producto', 'producto', 'anio', 'unidad',
                'valor', 'simbolo', 'descripcion_simbolo']

    # Lista de tuplas, en el orden correcto — sin iterrows
    datos = [tuple(x) for x in df[columnas].itertuples(index=False, name=None)]

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, datos)   # una sola llamada
        conn.commit()                     # un solo commit
        print(f'{cursor.rowcount} filas insertadas')
    except Error as e:
        conn.rollback()
        print(f'Error: {e}')
    finally:
        conn.close()








