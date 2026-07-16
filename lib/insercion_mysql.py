import mysql.connector
from mysql.connector import Error
import pandas as pd

### Inserción de datos en MySQL ### 

#nos conectamos a mySQL
def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
        #con ** pasamos como param a la fcón los valores del diccionario
        #es una desestructuración del diccionario, pasa de 1 vble(el dicc) a 5 vbles
    except Error as e:
        print(f'Error: {e}')
        return None



DB_CONFIG = {
    'host' : 'localhost',
    'port' : 3306,
    'user': 'root',
    'password': 'larisis5087',
    'database': 'proyecto_final'
}


def vaciar_tabla():
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




def insert_emission(emission):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute ("""insert 
                       into dataset_fao(
                       codigo_area, 
                       area, 
                       codigo_elemento, 
                       elemento, 
                       codigo_producto, 
                       producto, 
                       anio, 
                       unidad,
                       valor,
                        simbolo,
                        descripcion_simbolo) 
                       values
                       (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)""",(
                           emission['codigo_area'],
                           emission['area'],
                           emission['codigo_elemento'],
                           emission['elemento'],
                           emission['codigo_producto'],
                           emission['producto'],
                           emission['anio'],
                           emission['unidad'],
                           emission['valor'],
                           emission['simbolo'],
                           emission['descripcion_simbolo'])
                        )
                        
        conn.commit()
        #para sacar el libro que acabo de insertar necesito el id para consultar por get_by_id
        #last_id= cursor.lastrowid #te da el último id
        #result = get_book_by_id(last_id)
        #return result

    except Error as e:
        print(f'Error: {e}')
        return None
    finally:
        conn.close() 

