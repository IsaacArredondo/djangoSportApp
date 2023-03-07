Primero

'''
django-admin startproject sportspredictor
'''

Segundo

Entrar a la carpeta del proyecto sportspredictor y crear una app.

'''
cd sportspredictor
python manage.py startapp dashboard
'''

Ahora creamos el archivo que guardara las templates

'''
mkdir templates
'''

Y configuramos el archivo setting.py con la aplicación y la ruta de los TEMPLATES con:

'''
'DIRS': [BASE_DIR/'templates'],
'''

Y en INSTALLED_APPS

'''
'dashboard.apps.DashboardConfig',
'''

ahora agregamos los archivos html de para dashboard (index.html & prediction.html) y para partial (base.html & nav.html).


Y verificamos que la aplicación funcione con el comando:

'''
python manage.py runserver
'''

