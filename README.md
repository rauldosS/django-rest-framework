# 🏫 Django REST Framework

Projeto exemplo para entendimento e criação de aplicações Django com Django REST Framework.

![Django REST Framwork](https://github.com/rauldosS/django-rest-framework/blob/main/images/01.png?raw=true)

## 🗂️ Sumário

-  [📚 Conceitos](#-conceitos)
    - [📕 APIs](#-api)
    - [📗 REST - Representation Stare Transfer](#-rest---representation-stare-transfer)
    - [📘 Endpoints](#-endpoints)
        - [🗃️ Boas práticas na criação de endpoints](#-boas-práticas-na-criação-de-endpoints)
    - [🔖 Requests](#-requests)
        - [🔖 Versionamento de APIs](#-versão-da-api)
    - [🔖 Responses](#-responses)
    - [🔐 Segurança de APIs REST](#-segurança)
    - [🔖 Django REST Framework (DRF)](#-django-rest-framework-drf)
- [📖 Instalação e configuração básica](#-instalação-e-configuração)
- [📊 Configuração intermediária](#-configuração-intermediária)
    - [🔖 ViewSets](#-viewsets)
    - [🔖 Routers](#-routers)
    - [🔖 Relações](#-relações)
    - [🔖 Paginação](#-paginação)
- [🔐 Configuração avançada](#-configuração-avançada)
    - [🔖 Autenticação via Token](#-autenticação-via-token)
    - [🔖 Fazendo uso de permissões](#-fazendo-uso-de-permissões)
    - [🔖 Limitando número de requisições com Throttling](#-limitando-número-de-requisições-com-throttling)
    - [🔖 Customizando a validação dos dados](#-customizando-a-validação-dos-dados)
    - [🔖 Customizando a serialização dos dados](#-customizando-a-serialização-dos-dados)
- [👨‍💻 Testando APIs](#-testando-apis)
    - [🔖 Instalando e utilizando o módulo requests](#-instalando-e-utilizando-o-módulo-requests)
    - [🔖 Testando os métodos GET, POST, PUT e DELETE](#-testando-os-métodos-get-post-put-e-delete)
    - [🔖 Instalando e utilizando o módulo JSONPATH](#-instalando-e-utilizando-o-módulo-jsonpath)
    - [🔖 Testando com Pytest](#-testando-com-pytest)
    - [🔖 Insominia](#-insominia)
- [🕹️ Abrir e rodar o projeto escola](#-abrir-e-rodar-o-projeto)

---

# 📚 Conceitos

## 📕 API

Interface de comunicação de aplicações de forma programática.

## 📗 REST - Representation Stare Transfer

HTTP é um design sem estado, ou seja, toda requisição é única. A responsabilidade de lembrar dos estados é do cliente.

[Introdução às APIs REST](https://github.com/rauldosS/django-rest-framework/blob/main/docs/intro/02-introducao-as-apis-rest.pdf)

## 📘 Endpoints

### 🔖 Substantivos

> Gramática da língua portuguesa tem tudo a ver com endpoints, pois usamos <b>substantivos</b> e <b>verbos</b> para criá-los.

#### 🔖 Resources (recursos)

> Um `'resource'` pode ser, por exemplo, um modelo da nossa aplicação:

- Categorias
- Produtos

> Nós fazemos as operações CRUD através de `URI` específicas na nossa aplicação, por exemplo:

- sistema.com.br<b>/api/v1/produtos</b>
- sistema.com.br<b>/api/v1/categorias</b>

`Estas URIs são os endpoints`

### 🗃️ Boas práticas na criação de endpoints

> Um <b>endpoint</b> pode representar uma coleção de registros ou um registro individual.

> Coleção
```shell
sistema.com.br/api/v1/produtos
```
> Individual
```shell
sistema.com.br/api/v1/produtos/42
```

### 🔖 Verbos (CRUD)

Indica uma ação.

- `C` `Create` `POST`
- `R` `Read` `GET`
- `U` `Update` `PUT`
- `D` `Delete` `DELETE`

[Entendendo os Endpoints](https://github.com/rauldosS/django-rest-framework/blob/main/docs/intro/03-entendendo-os-endpoints.pdf)

## 📙 Requests

As requisições (requests) é a solicitação ao servidor.

<b>Exemplo:</b>

```shell
/api/v1/produtos?order=desc&limit=10
```

Tudo que vem depois do `?` é chamado de `querystring`

### 🔖 Cabeçalhos da request

- <b>Accept:</b> Específica o formato de arquivo.
- <b>Accept-Language:</b> Define lingua de retorno.
- <b>Cache-Control:</b> Específica se o conteúdo pode ser consumido do cache e em quanto tempo o cache é atualizado.

`application/json` define um padrão de retorno.

### 🔖 Versão da API

```shell
/api/v1/produtos
```
```shell
/api/v2/produtos
```

[Entendendo as Requests](https://github.com/rauldosS/django-rest-framework/blob/main/docs/intro/04-entendendo-as-requests.pdf)

## 📘 Responses

Preparar a Resposta.

> Detalhes avaliados da solicitação:

- Na requisição existe query string?
- Qual foi o verbo HTTP que realizou a ação?
- Quai são os dados do cabeçalho?
- Qual o formato requisitado?
- Preparar os dados da coleção ou indivíduo do recurso solicitado.

> Dados retornados:

- data (dados)
- Cabeçalho
    - Content-Type: Accept encaminhado.
    - Las-Modified: Data de criação ou última modificação.
    - Expires: Até quando este dado pode ser considerado atual
    - Status: 200 OK (código de status HTTP)

[Entendendo as Responses](https://github.com/rauldosS/django-rest-framework/blob/main/docs/intro/05-entendendo-as-responses.pdf)

## 🔐 Segurança

- Fazendo uso de cache.
- Limitar número de requisições por período (segundos).
- Autenticação (quem você é)
    - Token (chave publica)
- Autorização (o que você pode fazer)

[Entendendo sobre a segurança de APIs REST](https://github.com/rauldosS/django-rest-framework/blob/main/docs/intro/06-entendendo-sobre-a-seguranca-de-apis-rest.pdf)


## 📘 Django REST Framework (DRF)

`Model Serialization`, DRF mapeia os `Django Models` e provê uma facilidade muito grande a trabalhar com os objetos Python e serializar/deserializar para JSON.

---

# 📖 Instalação e configuração básica

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

---

# 📊 Configuração intermediária

## 🔨 ViewSets

[ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)

## 🔨 Routers

- Otimiza a criação de urls, gera automaticamente através do router as operações CRUD de apenas um modelo.
- Sobrescreva o método get para acessar, por exemplo, todas a avaliações de um determinado curso `(v2/cursos/1/avaliacoes)`.

## 🔨 Relações

> Existem 3 formas de retornar modelos relacionados em sua API.

### 🔖 Nested Relationship

> Retorna os objetos conforme parametrizado no seu Serializer das avaliações relacionadas.

```python
avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
```

### 🔖 HyperLinked Related Field

> Adicionar um link para acesso das avaliações relacionadas.

```python
avaliacoes = serializers.HyperlinkedRelatedField(
    many=True,
    read_only=True,
    view_name='avaliacao-detail'
)
```

### 🔖 Primary Key Related Field

> Adiciona apenas a chave primária (id) das avaliações relacionadas.

```python
avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
```

## 🔨 Paginação


> Em `escola/settings.py` adicione ao `REST_FRAMEWORK`:

```python
REST_FRAMEWORK = {
    ...,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

> Adiciona automaticamente 3 atributos ao retorno.

```python
{
    "count": "<int:contagem de páginas>",
    "next": "<link:página anterior>",
    "previous": "<link:próxima página>",
}
```

> <b>Obs:</b> Em métodos sobrescritos você deverá adicionar manualmente a paginação conforme exemplo que ocorre em `CursoViewSet`:

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

---

# 🔐 Configuração avançada

## 🔨 Autenticação via Token

> Configurações em `escola/settings.py`:

1. Adicionar aos INSTALLED_APPS:
```python
{
    ...,
    'rest_framework.authtoken',
    ...
}
```

2. Comentar autenticação via sessão do `REST_FRAMEWORK` e adicionar:
```python
'DEFAULT_AUTHENTICATION_CLASSES': (
    # 'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
),
```

3. Realizar migração
```shell
python manage.py migrate
```

### 🔖 Para sobrescrever o modelo User utilize

```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

admin = User.objects.get(id=1)

token = Token.objects.create(user=admin)

print(token.key)
```

> Token Admin: 11c573b2dab073aef36698a9600a43aa8cb70d99

> <b>Obs:</b> É possível realizar a criação via `Administração do Django`

## 🔨 Fazendo uso de permissões

> Permissões dizem respeito aos verbos HTTP (CRUD) que o usuário tem permissão para executar.

> Através do `Administração do Django` é possível realizar essa configuração de permissão sobre um modelo específico para cada usuário sem tornar o usuário administrador.

### 🔖 Criação de sua própria classe que define permissões

1. Criação de um arquivo chamado `permissions.py` no diretório do app
    1.1 Exemplo em `cursos/permissions.py`
2. Importação de módulo criado nas `views` e inserção no início do ViewSet
    2.1 Exemplo em `cursos/views.py`

```python
from rest_framework import permissions

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        EhSuperUser,
        permissions.DjangoModelPermissions,
    ),
    ...
```

## 🔨 Limitando número de requisições com Throttling

> Similar a permissões, porém ele vai limitar as requisições por um determinado período para os clientes.

> A configuração será global configurada no `REST_FRAMEWORK` em `cursos/settings.py`:

- Anônimos podem fazer podem fazer 5 requisições por minuto e
- Usuários autenticados podem fazer 10 requisições por minuto.

```python
{
    ...,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/minute',  # second, day, month, year
        'user': '10/minute'
    }
}
```

## 🔨 Customizando a validação dos dados

> <b>Restrição:</b> Avaliações não podem ser maior que 5 (avaliacao).

<b>Criação de uma avaliação:</b> 

```JSON
{
	"curso": 2,
	"nome": "Maria da Silva",
	"email": "maria@gmail.com",
	"avaliacao": 9
}
```

<b>Retorno:</b> 

```JSON
{
	"avaliacao": [
		"A avaliação precisa ser um inteiro entre 1 e 5"
	]
}
```

1. Em `cursos/seralizers.py` criar a validação para a classe
    1.1 A função por padrão deve começar com `validate_`

```python
def validate_avaliacao(self, valor):
    if valor in range(1, 6):  # 1, 2, 3, 4, 5
        return valor
    raise serializers.ValidationError('A avaliação precisa ser um inteiro entre 1 e 5')
```

## 🔨 Customizando a serialização dos dados

> Adicionar atributo no retorno com a `média das avaliações`

1. Criar atributo e especificar o tipo
```python
media_avaliacoes = serializers.SerializerMethodField()
```

2. Adicionar na lista de dados que serão apresentados
```python
fields = (
    'media_avaliacoes'
)
```

3. Criar função 
    3.1 Nome da função iniciado em _get e
    3.2 Restante do nome é o atributo que será criado

```python
def get_media_avaliacoes(self, obj):
    media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

    if media is None:
        return 0
    return round(media * 2) / 2
```

### 🔖 Sugestão de performance

> Ao inves de criar uma função para atualizar a média em cada requisição, criar um campo no modelo e atualizar o campo a cada atualização.

---

# 👨‍💻 Testando APIs

> A pasta `tests` no diretório raiz contém todos os testes com descrição em cada arquivo.

> Crie testes que façam sentido para a sua aplicação!

## 🔨 Instalando e utilizando o módulo requests

Módulo para fazer requisições.

```shell
pip install requests
```

[Arquivos de testes para requests](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests)

## 🔨 Testando os métodos GET, POST, PUT e DELETE

🔖[Testando o método GET](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests/get.py)
🔖[Testando o método POST](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests/post.py)
🔖[Testando o método PUT](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests/put.py)
🔖[Testando o método DELETE](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests/delete.py)

## 🔨 Instalando e utilizando o módulo JSONPATH

```shell
pip install jsonpath
```

> <b>Vantagem:</b> acessar diretamente os dados com maior facilidade e realizar filtros nativamente

[Arquivos de testes para jsonpath](https://github.com/rauldosS/django-rest-framework/blob/main/tests/jsonpath.py)

## 🔨 Testando com Pytest

```shell
pip install pytest
```

🔖[Pytest](https://github.com/rauldosS/django-rest-framework/blob/main/tests/requests/test_pytest.py)

> Comando para executar testes pelo arquivo pytest:

```shell
pytest .\tests\test_pytest.py
```

> <b>Obs:</b> o pk/id dos métodos PUT e POST (requests) deve ser atualizado para realização dos testes.

## 🔨 Insominia

[JSON de importação Insominia](https://github.com/rauldosS/django-rest-framework/blob/main/docs/escola.json)

---

# 🕹️ Abrir e rodar o projeto

**Instruções necessárias para abrir e executar o projeto**

> Instale o Python 3

1. Clone o repositório e entre na pasta:
```shell
git clone https://github.com/rauldosS/django-rest-framework.git
cd/django-rest-framework
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

## 🔖 Execução no ambiente Windows
![alt text](https://github.com/rauldosS/technical-test-nexxera/blob/main/images/01.gif?raw=true)