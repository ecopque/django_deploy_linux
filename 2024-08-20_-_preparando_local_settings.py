# my_project/schedule/local_settings.py: vamos abrir este aquivo.
# No terminal, vamos inserir este código para gerar uma senha aleatória que será utilizada em "settings.py" do Schedule Project (my_project). Comando: python3 -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));". #1: #2:
# Agora você vai em seu local_settings.py (# my_project/schedule/local_settings.py) e insere a nova chave no campo SECRET_KEY=. Veja abaixo: #3:
# my_project/schedule/local_settings.py:
# SECRET_KEY = 'Change-me'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xxx' #3: # my_project/schedule/settings.py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #4: # my_project/schedule/settings.py #4:
ALLOWED_HOSTS = ['00.00.000.000'] #5: # my_project/schedule/settings.py
# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xxx',
        'USER': 'user_xxx',
        'PASSWORD': 'xxx',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Agora no terminal, vamos acessar o servidor. #6:
