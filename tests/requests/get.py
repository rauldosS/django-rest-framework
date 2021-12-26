import requests

headers = {'Authorization': 'Token 11c573b2dab073aef36698a9600a43aa8cb70d99'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 2

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'