def eliminar_columnas(df, columnas):
    """
    Elimina las columnas especificadas de un DataFrame.

    Parámetros:
    df (pd.DataFrame): El DataFrame del cual se eliminarán las columnas.
    columnas (list): Lista de nombres de columnas a eliminar.

    Retorna:
    pd.DataFrame: DataFrame con las columnas eliminadas.
    """
    return df.drop(columns=columnas, errors='ignore')

def ver_cabecera(df):
    """
    Muestra la cabecera de un DataFrame.

    Parámetros:
    df (pd.DataFrame): El DataFrame del cual se mostrará la cabecera.
    """
    print(df.head())

def normalizar_columnas(df):
    nombre_columnas_normalizadas = [  'codigo_area', 
                       'area', 
                       'codigo_elemento', 
                       'elemento', 
                       'codigo_producto', 
                       'producto', 
                       'anio', 
                       'unidad',
                       'valor',
                        'simbolo',
                        'descripcion_simbolo']
    df.columns = nombre_columnas_normalizadas
    return df
