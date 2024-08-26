# ssh gnulinuxdebian@34.45.91.32 #1:
# sudo -u postgres psql #1:
# create role schedule_project_user with login superuser createdb createrole password 'schedule_project_user_password';. #2: #3: #4:
# create database schedule_project_dbname with owner schedule_project_user;. #5: #6:
# grant all privileges on database schedule_project_dbname to schedule_project_user;. #7: #8:
# \q #9:
# sudo systemctl restart postgresql #10: # \q
# nano ~/scheduleapp/schedule/local_settings.py #11: #12:
# Dentro do nano, vamos copiar todo o conteúdo de "# my_project/schedule/local_settings.py" e pressionar (ctrl + o) para salvar e (ctrl + x) para sair. Mais abaixo, veja o conteúdo de local_settings.py.
# Agora, no local_settings.py da sua máquina pode ser totalmente comentado.
# my_project/schedule/local_settings.py: 
# SECRET_KEY = 'Change-me'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_password' # my_project/schedule/settings.py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # my_project/schedule/settings.py
ALLOWED_HOSTS = ['34.00.00.00'] # my_project/schedule/settings.py
# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_db', #database
        'USER': 'user_schedule',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
