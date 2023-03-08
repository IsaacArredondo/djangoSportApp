Primero

```
django-admin startproject sportspredictor
```

Segundo

Entrar a la carpeta del proyecto sportspredictor y crear una app.

```
cd sportspredictor
python manage.py startapp dashboard
```

Ahora creamos el archivo que guardara las templates

```
mkdir templates
```

Y configuramos el archivo setting.py con la aplicación y la ruta de los TEMPLATES con:

```
'DIRS': [BASE_DIR/'templates'],
```

Y en INSTALLED_APPS

```
'dashboard.apps.DashboardConfig',
```

ahora agregamos los archivos html de para dashboard (index.html & prediction.html) y para partial (base.html & nav.html).


Y verificamos que la aplicación funcione con el comando:

```
python manage.py runserver
```

Despues creamos las vistas index.html y predictions.html en views.py del dashboard y creamos el archivo urls.py con las respectivas rutas en esta misma carpeta.

Asi mismo, tambien agregamos la ruta en el archivo urls.py del folder sportpredictor.

Agregamos el contenido de los archivos html.

Tambien agregamos el modelo Data y reflejamos el modelo creado en una base de datos con el comando:

```
python manage.py makemigrations
python manage.py migrate
```

Y creamos un manager del sistema con el comando:

```
python manage.py createsuperuser
```

Podemos como usuario: admin
correo: admin@gmail.com
pwd: admin

Y probamos que funcione correctamente el administrador de bases de datos.

Una vez funcionando correctamente registramos el modelo en el archivo models.py, y probamos agregar un registro en el administrador de bases de datos.

