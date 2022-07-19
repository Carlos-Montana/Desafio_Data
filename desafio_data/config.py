'''
En este archivo levantaremos todas la variables que se encuentan en el archivo .env,
para que despues sean usadas a lo largo del programa.
'''
from pathlib import Path
from decouple import config

#Datos de configuración base de datos postgres
DB = config('DB_CON')

#Urls de las distintas categorias
URL_CINE = config('CINE')
URL_MUSEO = config('MUSEO')
URL_BIBLIOTECA = config('BIBLIOTECA')

#Nombre de las tablas
TABLE_NAMES = ['tabla_raw', 'tabla_categoria', 'tabla_fuente', 'tabla_p_c', 'tabla_conf_cine']

#Root principal donde se encuentan los scripts,
#desde aca se manipula la rutan donde se encuentran los scripts sql
ROOT_DIR = Path(Path.cwd(), 'challenger_data')
