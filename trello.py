import os
import requests
from dotenv import load_dotenv

def read_boards(sessao):
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

def read_lists(sessao, quadro):
	parameters = {
		'field': ['name', 'id']
	}

	response = sessao.get(f'https://api.trello.com/1/boards/{quadro}/lists', params=parameters)

	if response.status_code == 200:
		data = response.json()

		for lst in data:
			print(f'Nome: {lst["name"]}')
			print(f'ID: {lst["id"]}')
	else:
		print('Não foi possível acessar as listas')

def read_cards(sessao, lista):
	parameters = {
		'field': ['name', 'id']
	}

	response = sessao.get(f'https://api.trello.com/1/lists/{lista}/cards', params=parameters)

	if response.status_code == 200:
		data = response.json()

		for crt in data:
			print(f'Nome do cartão: {crt["name"]}')
			print(f'ID: {crt["id"]}')
	else:
		print('Não foi possível acessar os cartões')

def create_board(sessao, nome, descricao):
	parameters = {
		'name': nome,
		'desc': descricao
	}

	response = sessao.post('https://api.trello.com/1/boards', params=parameters)

	if response.status_code == 200:
		data = response.json()

		print(f'Nome: {data["name"]}')
		print(f'Descrição: {data["desc"]}')
	else:
		print('Não foi possível criar o quadro')

def create_list(sessao, nome, quadro):
	parameters = {
		'name': nome,
		'idBoard': quadro
	}

	response = sessao.post('https://api.trello.com/1/lists', params=parameters)

	if response.status_code == 200:
		data = response.json()

		print(f'Nome da lista: {data["name"]}')
		print(f'ID da lista: {data["id"]}')
	else:
		print('Não foi possível adicionar a lista')

def create_card(sessao, nome, descricao, lista):
	parameters = {
		'name': nome,
		'desc': descricao,
		'idList': lista
	}

	response = sessao.post('https://api.trello.com/1/cards', params=parameters)

	if response.status_code == 200:
		data = response.json()

		print(f'Nome do cartão: {data["name"]}')
		print(f'Descrição do cartão: {data["desc"]}')
	else:
		print('Não foi possível adicionar o cartão')