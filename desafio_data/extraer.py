'''
Este archivo contine la parte de la extracción

'''
import logging
from pathlib import Path
from datetime import datetime
import requests
from config import ROOT_DIR


#extraer.py
def crea_directorio(categoria: str) -> Path:
    '''
    Esta función controla la creación del directoria donde se guardaran
    los archivos.

    Args:
        categoria (str): nombre del directoria el cual es su categoria

    Returns:
        root_dir: retorna el path donde se guardara el archivo
    '''
    anio_mes = datetime.now().strftime('%Y-%B')
    root_dir = Path(ROOT_DIR, categoria,anio_mes)
    root_dir.mkdir(parents= True, exist_ok= True)
    return root_dir

def cargar_archivo(categoria: str, url: str, root_dir: Path) -> Path:
    '''
    Esta función controla la carga del archivo el cual crea el archivo,
    descarga el contenido de la url y la carga en el .csv

    Args:
        categoria (str): nombre de la categoria, por ejemplo: museos
        url (str): la url para descargar el recurso
        root_dir (Path): la ruta donde se cargara y guardara

    return:
        archivo (path): devuelvo la ruta del archivo, luego se usa para la transformación y carga
    '''
    #logging.info('Creando y cargando el archivos')
    cat_fecha = f'{categoria}'+'-'+datetime.now().strftime('%d-%m-%Y')+'.csv'
    archivo = Path(root_dir, cat_fecha)
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    try:
        with open(archivo, 'w', encoding='utf-8') as arch:
            arch.write(resp.text)
        #logging.info('Carga satisfactoria')
    except OSError:
        logging.info('OSError, no se pede abrir el archivo')
    return archivo

def extraer(mi_dict: dict) -> dict:
    '''
    Esta funcion es para el primer paso del etl, la extracción, crear los directorios si no existen
    y crea también el archivo

    Args:
        mi_dict (dict): diccionario con las urls para extraer
    return:
        dict_path (dict): diccionario con key = nombre_categoria y value = path
    '''

    dict_path = {}
    for i in mi_dict.keys():
        root_dir = crea_directorio(i)
        dict_path[i] = cargar_archivo(i, mi_dict[i], root_dir)
    logging.info('Termino el extract satisfatoriamente')
    return dict_path
