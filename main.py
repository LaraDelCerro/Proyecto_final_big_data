#Datos: https://www.fao.org/faostat/es/#data/GLE


from lib.carga_datos import df_continentes 
from lib.limpieza_datos import eliminar_columnas,normalizar_columnas
import pandas as pd
import mysql.connector
from mysql.connector import Error
from lib.insercion_mysql import insert_emissions, vaciar_tabla

print(df_continentes.head())  # Muestra las primeras filas del DataFrame original

df_continente_sin_columnas= eliminar_columnas(df_continentes, ['Código del ámbito', 'Ámbito', 'Código del año', 'Código fuente', 'Fuente', 'Nota'])  # Elimina las columnas especificadas


print(df_continente_sin_columnas.head()) #Compruebo que las columnas han sido eliminadas


#convertir a csv. Genera un archivo continente.csv
df_continente_sin_columnas.to_csv('./continentes.csv', index=False)

df_normalizado = normalizar_columnas(df_continente_sin_columnas)

vaciar_tabla()  # Llama a la función para vaciar la tabla antes de insertar nuevos registros



insert_emissions(df_normalizado) #inserción de todos los registros en la base de datos