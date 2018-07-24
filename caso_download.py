import requests
import sys
from bs4 import BeautifulSoup


def get_test(problem):
    url = 'https://www.urionlinejudge.com.br/repository/UOJ_' + problem + '.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.findAll("table")
    casos = list()
    for table in tables:
        caso = {'entrada': table.findAll(
            "p")[0].text.lstrip() + '\n', 'saida': table.findAll("p")[1].text.lstrip() + '\r\n'}
        casos.append(caso)
    f = open("casos_" + problem + ".py", "w+")
    f.write("casos = " + str(casos))
    f.close()
    print('Casos criados com sucesso\n' + casos)
    h = open(problem + ".py", "a+")
    default_text = '''
	 # -*- coding: utf-8 -*-
	\'''
	Escreva a sua solução aqui
	Code your solution here
	Escriba su solución aquí
	\'''
	'''
    h.write("casos = " + str(casos))
    h.close()

get_test(sys.argv[1])
