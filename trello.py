import os
import requests
from dotenv import load_dotenv

def push_boards(sessao):
	parameters = {
		'field': ['name', 'url']
	}

	response = sessao.get(f'https://api.trello.com/1/members/me/boards', params=parameters)

	if response.status_code == 200:
		data = response.json()

		for board in data:
			print(f'Nome: {board["name"]}')
			print(f'URL: {board["url"]}')
			print(f'ID: {board["id"]}')
	else:
		print('Ocorreu um erro na requisição')

def create_board(sessao, nome, descricao):
	parameters = {
		'name': nome,
		'desc': descricao
	}

	response = sessao.post('https://api.trello.com/1/boards', params=parameters)

	if response.status_code == 200:
		data = response.json()

		print('O quadro foi criado:')

		print(f'Nome: {data["name"]}')
		print(f'Descrição: {data["desc"]}')
		print(f'URL: {data["url"]}')
		print(f'ID: {data["id"]}')