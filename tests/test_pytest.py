import requests
import random


class TestCursos:
    headers = {'Authorization': 'Token 11c573b2dab073aef36698a9600a43aa8cb70d99'}
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Programação com Ruby 1",
            "url": "http://www.geekuniversity.com.br/ruby-1"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 2",
            "url": "http://www.geekuniversity.com.br/ruby-2"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Novo Curso de Ruby 3",
            "url": "http://www.geekuniversity.com.br/ruby-3"
        }

        resposta = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}12/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0