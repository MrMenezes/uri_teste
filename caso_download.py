import requests
import sys
import os
from bs4 import BeautifulSoup


def unicodetoascii(text):

    uni2ascii = {
        ord(b'\xe2\x80\x99'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\x9c'.decode('utf-8')): ord('"'),
        ord(b'\xe2\x80\x9d'.decode('utf-8')): ord('"'),
        ord(b'\xe2\x80\x9e'.decode('utf-8')): ord('"'),
        ord(b'\xe2\x80\x9f'.decode('utf-8')): ord('"'),
        ord(b'\xc3\xa9'.decode('utf-8')): ord('e'),
        ord(b'\xe2\x80\x9c'.decode('utf-8')): ord('"'),
        ord(b'\xe2\x80\x93'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\x92'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\x94'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\x94'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\x98'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\x9b'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\x90'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\x91'.decode('utf-8')): ord('-'),
        ord(b'\xe2\x80\xb2'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\xb3'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\xb4'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\xb5'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\xb6'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x80\xb7'.decode('utf-8')): ord("'"),
        ord(b'\xe2\x81\xba'.decode('utf-8')): ord("+"),
        ord(b'\xe2\x81\xbb'.decode('utf-8')): ord("-"),
        ord(b'\xe2\x81\xbc'.decode('utf-8')): ord("="),
        ord(b'\xe2\x81\xbd'.decode('utf-8')): ord("("),
        ord(b'\xe2\x81\xbe'.decode('utf-8')): ord(")"),

    }
    return text.translate(uni2ascii).encode('ascii', 'ignore').decode('utf-8')


def get_test(problem):
    url = 'https://www.urionlinejudge.com.br/repository/UOJ_' + problem + '.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('h1').text
    descricao = soup.find(
        "div", {"class": "description"}).find('p').text.lstrip()
    entrada = soup.find("div", {"class": "input"}).find('p').text.lstrip()
    saida = soup.find("div", {"class": "output"}).find('p').text.lstrip()
    print(title)
    tables = soup.findAll("table")
    casos = list()
    for table in tables:
        if len(table.findAll("p")) > 0:
            caso = {'entrada': '\n'.join(list(map(str.lstrip, table.findAll("p")[0].text.lstrip().split(
                '\n')))) + '\n', 'saida': '\n'.join(list(map(str.lstrip, table.findAll("p")[1].text.lstrip().split('\n')))) + '\r\n'}
            casos.append(caso)
    f = open("casos_" + problem + ".py", "w+")
    if len(casos) == 0:
        casos = '[]'
    f = open("casos_" + problem + ".py", "w+")
    f.write("#" + title)
    f.write("\n" + "casos = " + str(casos))
    f.write("\n\n'''Descição:" + unicodetoascii(descricao) + "'''")
    f.write("\n\n'''Entrada:" + unicodetoascii(entrada) + "'''")
    f.write("\n\n'''Saida:" + unicodetoascii(saida) + "'''")
    f.close()
    print('Casos criados com sucesso!\n' + str(casos))
    if not os.path.exists(problem + ".py"):
        h = open(problem + ".py", "w+")
        default_text = '''# -*- coding: utf-8 -*-
\'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
\'''
'''
        h.write(default_text)
        h.close()
        print(problem + '.py\t Criado com sucesso!')
    else:
        print(problem + '.py\t Já estava criado!')

get_test(sys.argv[1])
