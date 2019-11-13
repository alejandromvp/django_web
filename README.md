#link curso
https://tutorial.djangogirls.org/es/installation/#brief-intro-to-the-command-line
# django_web
 creando sitio web utilizando tecnologia web django
#notas:
-al agregar una startapp, se debe agregar en settings->INSTALLED_APPS en el cual se incluye nombre de modelo, y apps.py

#instalar virtualenv
python -m venv myvenv

#instalar django
pip install django
pip install Django~=2.2.4

#trabajar con virtualenv
myvenv\Scripts\activate

#crear proyecto
django-admin.exe startproject mysite

#crear migracionse crea archivo sqlite3)
python manage.py migrate

#iniciar servidor
python manage.py runserver

#$crear applicacion dentro de proyecto
python manage.py startapp blog

#agregar modelo creado en app en la bd (migration)
python manage.py makemigrations blog
python manage.py migrate blog

#crear super usuario
python manage.py createsuperuser