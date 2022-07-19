'''
Este script crea la conexion a la base de datos y las tablas necesarias
'''
import logging
from pathlib import Path
from sqlalchemy import create_engine
from config import ROOT_DIR, TABLE_NAMES, DB



#script.py
#La idea leer los archivos creados y crear las tablas requeridas
def crear_tablas() -> None:
    '''
    Función que crea las tablas
    '''
    root_scripts = Path(ROOT_DIR,'sql')
    engine = create_engine(DB)
    with engine.connect() as con:
        try:
            for tabla in TABLE_NAMES:
                with open(Path(root_scripts, tabla+'.sql'), 'r', encoding='utf-8') as archivo:
                    engine.execute(archivo.read())
        except OSError:
            logging.info('No se puedo abrir archivo')
    logging.info('Tablas creadas correctamente')
#Llamando a la funcion que crea las tablas.
if __name__ == "__main__":
    #Pregunto si existe el archivo, no es la ruta adecuada y tiene que subir un nivel
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
    crear_tablas()
