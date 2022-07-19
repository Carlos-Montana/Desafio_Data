'''
Este archivo contiene la parte de transformar
'''
import logging
from pathlib import Path
from sqlalchemy import create_engine
from config import DB, ROOT_DIR
import pandas as pd


#transformar.py
engine = create_engine(DB)
new_columns = ['cod_localidad',
'id_provincia',
'id_departamento',
'categoría',
'provincia',
'localidad',
'nombre',
'domicilio',
'código postal',
'número de teléfono',
'mail',
'web']


def guardar(df_cat: pd.DataFrame, categoria: str) -> Path:
    '''
    Función que guarda el Dataframe transformado en el directorio transform
    para que luego sea ocupado por la función de cargar la base de datos.

    Args:
        df (pd.DataFrame): Dataframa transformado para guardar
        categoria (str): La categoria para guardarlo con ese nombre

    Returns:
        Path: _description_
    '''
    #Guarda el archivo en un csv
    root_t = Path(ROOT_DIR, 'transform')
    root_t.mkdir(parents=True, exist_ok=True)
    archivo = Path(root_t, categoria+'.csv')
    df_cat.to_csv(archivo, index=False)
    return archivo

#Museos tiene una configuracion diferente, 
#los nombres de la mayoria de las columnas diferentes a los demas dfs
def normaliza_df_museo(ruta: Path) -> pd.DataFrame:
    '''
    Función especifica para normalizar el nombre de las columnas, que devuelve
    un dataframe para que se guarde como .csv y se ocupado por la función cargar.

    Args:
        ruta (Path): Ruta donde se encuentra el .csv crudo de la categoria ej. museos

    Returns:
        pd.DataFrame: Dataframe listo para guardar en el directorio transform
        donde luego se leera en la función de cargar la base de datos
    '''
    df_m = pd.read_csv(ruta, usecols=['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria',
            'provincia', 'localidad', 'nombre','direccion', 'CP', 'telefono', 'Mail', 'Web',])
    df_m.columns = new_columns
    return df_m

def normaliza_dfs(ruta: Path, categoria: str) -> pd.DataFrame:
    '''
    Función especifica para normalizar el nombre de las columnas, que devuelve
    un dataframe para que se guarde como .csv y se ocupado por la función cargar.

    Args:
        ruta (Path): Ruta donde se encuentra el .csv crudo de la categoria ej. cines
        categoria (str): Nombre de la categoria ej. cines

    Returns:
        pd.DataFrame: Dataframe listo para guardar en el directorio transform
        donde luego se leera en la función de cargar en la base de datos
    '''
    df_cat = pd.read_csv(ruta)
    #Cambiando el nombre a las columnas
    if categoria == 'cines':
        df_cat = df_cat[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría','Provincia',
                 'Localidad', 'Nombre','Dirección', 'CP', 'Teléfono', 'Mail', 'Web']]
        df_cat.columns = new_columns
    else:
        df_cat = df_cat[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría','Provincia',
                 'Localidad', 'Nombre','Domicilio', 'CP', 'Teléfono', 'Mail', 'Web']]
        df_cat.columns = new_columns
    return df_cat

def transformar(rutas: dict) -> dict:
    '''
    Funcion principal encargada de realizar y utilizar otras funciones
    para poder realizar las transformaciones pedidas en el challenger

    Args:
        rutas (dict): Diccionario con las rutas de las categorias

    Returns:
        dict: Diccionario con las rutas de las categorias transformadas,lista para cargar
    '''
    dict_t = {}#aca guardamos las rutas de los csv tranformados para que los levantemos de cargar
    for categoria in rutas.keys():
        if categoria == 'museos':
            df_cat = normaliza_df_museo(rutas[categoria])
        else:
            df_cat = normaliza_dfs(rutas[categoria], categoria)
        dict_t[categoria] = guardar(df_cat, categoria)

    logging.info('Transformación terminada satisfactoriamente')
    return dict_t
