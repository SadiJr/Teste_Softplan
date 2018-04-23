# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
from operator import itemgetter
#import collections
#from selenium import webdriver
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

import re

url_base = "https://www.youtube.com/results?search_query=Chitãozinho+e+Chororó"
urls = []
nomes = []
visualizacoes = []

conexao = requests.get(url_base)
sopa_dados = BeautifulSoup(conexao.text, 'html.parser')
dados = sopa_dados.findAll('a', attrs={'class':'yt-uix-tile-link'})

for i in dados:
    url = "https://www.youtube.com" + i['href']
    urls.append(url)
    nome = i['title']
    nomes.append(nome)
for i in range(0, len(urls)):
    #print(urls[i])
    #print(nomes[i])
    conexao = requests.get(urls[i])
    sopa_videos = BeautifulSoup(conexao.text, 'html.parser')
    visu = sopa_videos.find('div', class_="watch-view-count")
    if(visu == None):
        visualizacoes.append(0)
    #    print('É um usuário')
    else:
        visu = visu.text
        visu = int(re.sub('[^0-9]', '', visu))
    #    print(visu)
    #    print(type(visu))
        visualizacoes.append(visu)
    #print('-'*100)

dic = {}
for i in range(0, len(nomes)):
    dic[visualizacoes[i]] = {nomes[i]}

print('Ordenamento:\n')
sorte = sorted(dic.items(), key=itemgetter(0))
for c in sorte:
    print(c)