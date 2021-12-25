# Escola

Escola com Django REST Framework

## Instalação e configuração

1. Instale o django-rest-framework
```shell
pip install djangorestframework markdown django-filter
```

```shell
pip freeze > requirements.txt
```

2. Adicionar `rest_framework` em `INSTALLED_APPS` no arquivo `escola/settings.py`

```python
[
    'django_filters',
    'rest_framework'
]
```

3. Adicionar configurações de `DRF` no arquivo `escola/settings.py`

```python
# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}
```

4. Incluir URLs padrão em `urlpatterns` no arquivo `escola/urls.py`

```python
path('auth/', include('rest_framework.urls')),
```



## 🔨 Funcionalidades

## 🛠️ Abrir e rodar o projeto

**Instruções necessárias para abrir e executar o projeto**

> Instale o Python 3

1. Clone o repositório e entre na pasta:
```shell
git clone https://github.com/rauldosS/technical-test-nexxera.git
cd technical-test-nexxera
```

2. Crie um ambiente virtual:
> Linux
```shell
virtualenv <nome_da_virtualenv>
```

> Windows
```shell
python -m venv <nome_da_virtualenv>
```

3. Ative o ambiente virtual que você acabou de criar:
> Linux
```shell
source <nome_da_virtualenv>/bin/activate
```

> Windows
```shell
.\<nome_da_virtualenv>\Scripts\activate
```

4. Instale os pacotes de desenvolvimento local:
```shell
pip install -r requirements.txt
```

5. Execute as migrações:
```shell
python manage.py migrate
```

Rode o servidor de desenvolvimento:
```shell
python manage.py runserver
```

### 📍 Execução no ambiente Windows
![alt text](https://github.com/rauldosS/technical-test-nexxera/blob/main/images/01.gif?raw=true)