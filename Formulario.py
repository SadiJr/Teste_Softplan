from bs4 import BeautifulSoup
import requests
import time
import re
from selenium import webdriver

url = "https://docs.google.com/forms/d/e/1FAIpQLSclXidd6MZ_C8t7l_7OVtTKbAbJSqGry3d85kfb8VqmigPDug/viewform"
url_envio = "https://docs.google.com/forms/d/e/1FAIpQLSclXidd6MZ_C8t7l_7OVtTKbAbJSqGry3d85kfb8VqmigPDug/postResponse"
urls = []
conexao = requests.get(url)
sopa = BeautifulSoup(conexao.text, 'html.parser')
dados = sopa.findAll('div', class_={'freebirdFormviewerViewItemsItemItemTitle freebirdCustomFont'})
for i in dados:
    urls.append(i.a['href'])
urls2 = []
for i in urls:
    conexao = requests.get(i)
    sopa = BeautifulSoup(conexao.text, 'html.parser')
    redirecao = sopa.body
    redirecao = redirecao.text
    redirecao = redirecao[20:]
    urls2.append(redirecao)
respostas = []
for i in urls2:
    print(i)
    conexao = requests.get(i)
    sopa = BeautifulSoup(conexao.text, 'html.parser')
    resposta = sopa.find('title')
    resposta = resposta.text
    resposta = resposta.replace(' - YouTube','')
    respostas.append(resposta)
print(respostas)
conexao = requests.get(url)
sopa = BeautifulSoup(conexao.text, 'html.parser')
dados = sopa.findAll('div', class_={'quantumWizTogglePaperradioEl docssharedWizToggleLabeledControl freebirdThemedRadio freebirdThemedRadioDarkerDisabled freebirdFormviewerViewItemsRadioControl'})
questoes = 0
submicao = {}
for i in range(0,4):
    opcao = dados[questoes]['aria-label']
    if(opcao == respostas[i]):
        submicao[dados[0]['aria-checked']] = {'true'}
        print(respostas[i])
        print(opcao == respostas[i])
        print('-'*100)
        print('*' * 100)
        print('-' * 100)
    else:
        auxiliar = questoes
        auxiliar = auxiliar + 1
        dados[1]['aria-checked'] = True
        print(respostas[i])
        submicao[dados[auxiliar]['aria-checked']] = {'true'}
        print(dados[auxiliar]['aria-label'] == respostas[i])
        print('-' * 100)
        print('*' * 100)
        print('-' * 100)
    questoes = questoes + 2

requests.post(url_envio, submicao)
