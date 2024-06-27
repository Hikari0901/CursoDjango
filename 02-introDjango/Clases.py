""".
pasos:
1.crear entorno virtual:
Python -m venv (nombre) #crea entorno
pip list #lista de paquetes en el entorno
deactivate #desactivar el entorno
ls #lsita de carpetas y archivos
#esquema MVT:
Modelo-Vista-Template

vista: logica del negocio
modelo: sentencia sql
plantilla: template para renderizar la info.

2.Crear el proyecto con Django

django-admin startproject (nombre del proyecto) #en la terminal

3. levantar server
estar en la raiz del proyecto, en el archivo manage.py
python manage.py runserver
acceder al server: cntrl + click izquierdo en la ruta http en la terminal

#funcion de los archivos:
manage.py.-documento padre para levantar los demas documentos del proyecto(se lo modifica para levantar el server a produccion)
__init__.py.- indica que es un modulo y es vacio
settings.py.- va la config de Django(se lo modifica mas)
    istalled_apps.- se modifica al instalar una app
    secretkey.- se usa una llave para que funcione el codigo en produccion
    templates.- se modifica para llamar a la modificacion del template
    databases.- se configura las bases de datos
    apppasswordvalidator.- seguridad de datos de django
    language_code.- configura el idioma del sitio web
    static_url.-para cargar mas archivos para renderizar(se colocan las rutas)
urls.py.- administra las urls del sitio web(permite crear mas urls)
asgi.py.- es una config para ser compatible con cualquier navegador
wsgi.py.- se peude hacer compatible con cualquier server para alojar la app(inclutendo de paga)
db.sqlite3.- una base de datos que se crea por defecto

4.- crear app


"""
