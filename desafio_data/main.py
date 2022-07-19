'''
Este archivo es el main y maneja todo el programa
'''
import logging
from pathlib import Path
from config import URL_CINE, URL_MUSEO, URL_BIBLIOTECA
from extraer import extraer
from transformar import transformar
from cargar import cargar

#main.py

#Diccionario con las urls de las categorias para descargar los csv
categorias = {'museos':URL_MUSEO, 'cines':URL_CINE, 'bibliotecas':URL_BIBLIOTECA}
def main():
    '''
    Funcion principal se encarga de ir llamando a las distintas
    fases del etl, como extraer, transformar y cargar
    '''
    logging.info('Comenzando ...')
    logging.info('Extrayendo')
    rutas = extraer(categorias)
    logging.info('Transformando')
    rutas_t = transformar(rutas)#devuelve ruta con csv transforamada
    logging.info('Cargando')
    cargar(rutas['cines'], rutas_t)

if __name__=='__main__':
    #Pregunto si existe el archivo, si es TRUE no es la ruta adecuada y tiene que subir un nivel
    if Path('script.py').exists():
        raise FileExistsError ('Error al ejecutar, tiene que subir un nivel')

    #Configuración logging para escribir en archivo .log
    logging.basicConfig(
        format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
        level  = logging.INFO,
        filemode = "a"
        )
    if logging.getLogger('').hasHandlers():
        logging.getLogger('').handlers.clear()
    fh = logging.FileHandler('logs.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)-5s %(name)-5s %(levelname)-5s %(message)s'))
    logging.getLogger('').addHandler(fh)
    main()
