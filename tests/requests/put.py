import requests

headers = {'Authorization': 'Token 11c573b2dab073aef36698a9600a43aa8cb70d99'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "Novo Curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 6
curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']