'''
En este archivo se carga la información en la base de datos postgres
'''
import logging
from datetime import datetime
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from config import DB


#cargar.py

fecha = datetime.now().strftime('%Y-%m-%d')#fecha de carga
engine = create_engine(DB)

def cargar_cine(ruta_cine: Path) -> None:
    '''
    Función que se encarga de poblar la base de datos que tiene los
    requirimientos para la categoria cine

    Args:
        ruta_cine (Path): Ruta del archivo.csv crudo para extraer el requirimiento
        y cargarlo en la base de datos.
    '''
    df_cine = pd.read_csv(ruta_cine)
    df_cine = df_cine.groupby('Provincia', as_index=False)\
                                [['Pantallas', 'Butacas', 'espacio_INCAA']].count()
    df_cine['create_at'] = fecha
    df_cine.to_sql(name='tabla_conf_cine', con=engine, if_exists='replace', index=False)

def cargar(ruta_cine: Path, rutas_t: dict) -> None:
    '''
    Función principal que se encarga de cargar la base de datos con todas 
    las tablas requeridas.

    Args:
        ruta_cine (Path): Ruta donde se encuentra el archivo.csv crudo de cines
        rutas_t (dict): Diccionario con las rutas de los archivos.csv transformados
        listo para ser cargados en las tablas de la base de datos.
    '''
    #Cargando cines
    cargar_cine(ruta_cine)

    #Cargando todos los dfs para realizar las metricas requeridas, y cargarlas en la db
    lista_dfs = []
    for categoria in rutas_t.keys():
        df_cat = pd.read_csv(rutas_t[categoria])
        lista_dfs.append(df_cat)

    #Aca concateno los dfs
    all_dfs = pd.concat(lista_dfs, axis=0)

    #Cantidad de registros totales por categoría
    df_mod = all_dfs.groupby('categoría', as_index=False).size()
    df_mod['create_at'] = fecha
    df_mod.to_sql('tabla_categoria', con=engine, if_exists='replace', index=False)

    #Cantidad de registros por provincia y categoría
    df_mod = all_dfs.groupby(['categoría', 'provincia'], as_index=False).size()
    df_mod['create_at'] = fecha
    df_mod.to_sql('tabla_p_c', con=engine, if_exists='replace', index=False)

    #Cantidad de registros totales por fuente
    lista_size = []
    for cont, df_cat in enumerate(lista_dfs):
        temp = df_cat.size
        lista_size.append(temp)
    df_mod = pd.DataFrame({'Fuentes': list(rutas_t.keys()),
                    'Total': lista_size })
    df_mod['create_at'] = fecha
    df_mod.to_sql(name='tabla_fuente', con=engine, if_exists='replace', index=False)

    #Aca cargos todos los dfs concatenados
    all_dfs['create_at'] = fecha
    all_dfs.to_sql(name='tabla_raw', con=engine, if_exists='replace', index=False)

    logging.info('Carga teminada satisfactoriamente')
