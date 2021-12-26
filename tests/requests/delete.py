import requests

headers = {'Authorization': 'Token 11c573b2dab073aef36698a9600a43aa8cb70d99'}
url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

print(resultado.text)

# Testando se o tamanho do conteúdo retorno é 0
assert len(resultado.text) == 0