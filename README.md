# Escola

Escola com Django REST Framework

# 🛠️ Instalação e configuração

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

# 🛠️ Configuração intermediária

## 🔨 ViewSets

[ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)

## 🔨 Routers

- Otimiza a criação de urls, gera automaticamente através do router as operações CRUD de apenas um modelo.
- Sobrescreva o método get para acessar, por exemplo, todas a avaliações de um determinado curso `(v2/cursos/1/avaliacoes)`.

## 🔨 Relações

Existem 3 formas de retornar modelos relacionados em sua API.

### 📍 Nested Relationship

Retorna os objetos conforme parametrizado no seu Serializer das avaliações relacionadas.

```python
avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
```

### 📍 HyperLinked Related Field

Adicionar um link para acesso das avaliações relacionadas.

```python
avaliacoes = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='avaliacao-detail'
)
```

### 📍 Primary Key Related Field

Adiciona apenas a chave primária (id) das avaliações relacionadas.

```python
avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

## 🔨 Paginação

Em `escola/settings.py` adicione ao `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

Adiciona automaticamente 3 atributos ao retorno.

```python
{
    "count": "<int:contagem de páginas>",
    "next": "<link:página anterior>",
    "previous": "<link:próxima página>",
}
```

Obs: Em métodos sobrescritos você deverá adicionar manualmente a paginação conforme exemplo que ocorre em `CursoViewSet`:

```python
@action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
```

# 🛠️ Configuração avançada

# 🔨 Funcionalidades

# 🛠️ Abrir e rodar o projeto

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

## 📍 Execução no ambiente Windows
![alt text](https://github.com/rauldosS/technical-test-nexxera/blob/main/images/01.gif?raw=true)