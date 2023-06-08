import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from datetime import date


u = 'https://asloterias.com.br/resultados-da-mega-sena-'
html_list = []
ano = 1996
data = date.today().year
for p in range(1, (2022 - 1996)):
    lista=[]
    req = Request(u + str(ano + p), headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    site = BeautifulSoup(html.read(), 'html.parser')
    lista.append(site.find_all('span', {'class': 'dezenas dezenas_mega'}))
    html_list.append(lista)

lista = []
for a in range(len(html_list)):
    for i in html_list[a][0]:
        lista.append(i)

numeros = []
for i in range(len(lista)):
    numeros.append(lista[i].text)

n = enumerate(numeros)
df = pd.DataFrame(list(n))
num = df.value_counts(df[1]).head(15)
num = pd.DataFrame(num)
num = num.reset_index()

list_num=[]
limite = 6
while len(list_num) < limite:
    n = int(num[1].sample())
    if n not in list_num:
        list_num.append(int(n))

print(list_num) 