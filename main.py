from lib.carga_datos import df_continentes 
from lib.limpieza_datos import eliminar_columnas,normalizar_columnas
import pandas as pd
import mysql.connector
from mysql.connector import Error
from lib.insercion_mysql import insert_emission, vaciar_tabla

print(df_continentes.head())  # Muestra las primeras filas del DataFrame original

df_continente_sin_columnas= eliminar_columnas(df_continentes, ['Código del ámbito', 'Ámbito', 'Código del año', 'Código fuente', 'Fuente', 'Nota'])  # Elimina las columnas especificadas


print(df_continente_sin_columnas.head())

#ver_cabecera(df_continente_sin_columnas)  # Muestra la cabecera del DataFrame después de la limpieza

#convertir a csv
df_continente_sin_columnas.to_csv('./continentes.csv', index=False)

df_normalizado = normalizar_columnas(df_continente_sin_columnas)

vaciar_tabla()  # Llama a la función para vaciar la tabla antes de insertar nuevos registros



#insert_emission(df_normalizado.iloc[0].to_dict()) #inserción de un registro en la base de datos, se pasa a diccionario pq la función insert_emission espera un diccionario

#inserción de todos los registros en la base de datos
for index, row in df_normalizado.iterrows():
    #print(index)
    insert_emission(row.to_dict())  