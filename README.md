# Challenger-Data

## Librerias utilizadas
Todas las librerias utilizadas estan especificadas en pyproject.toml o requirements.txt

## Poner en marcha el proyecto

- ### *Puedes leer el siguiente enlace que explica el reto -->* [challenger](desafio.md)<br>

- ### Clonar el repositorio en su directorio local

- ### El archivo .env.ex quitarle el .ex para poder utilizarlo
    Este archivo contiene todas las configuraciones necesarias para que corran los scripts

- ### Logs y Excepciones
    Todos los logs capturados se guardan en la un fichero .log.

- ### Entorno vitual (poetry)
    Para poder desplegar el proyecto en un entorno vitual con todas las librerias correctamente, usaremos en este caso poetry.<br>
    Para instalar poetry use `pip install poetry` <br>
    Ahora dentro de la carpeta donde clono el repositorio ejecutamos `poetry install` y luego para acceder al entorno virtual `poetry shell`.<br>
    *Tambien puede utilizar otro entorno vitual.*<br>

- ### La base de datos (postgres)
    Para crear la base de datos que en este caso se uso postgres, y docker para levantar un contenedor de la imagen, para ello tener docker instalado y con el siguiente comando se levanta la imagen de postgres de manera sencilla<br> `docker run --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -p 5432:5432 postgres:14` <br>
    Para levantar una imagen y que los datos persistan ejecutamos el siguiento comando <br>
    `docker run --name postgres -v db-data:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres postgres:14` <br>
    Para interactuar con la base de datos puedes usar un programa como DBeaver o puedes hacer desde la linea de comando con el siguiente comando <br>
    `docker excec -it postgres psql -U postgres -d postgres` <br>
    **los archivos.sql se encuentran en desafio_data/sql**

- ### Crear la base de datos con scrip.py
    Para hacerlos tienes que ejecutar el siguiente comando <br>
    `python desafio_data/script.py`

- ### Correr el programa principal(main.py)
    Ahora solo queda correr el siguiente archivo para correr el programa principal, de la siguiente manera <br>
    `python desafio_data/main.py`