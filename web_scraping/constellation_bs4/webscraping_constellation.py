from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://constellation.com.br/pra-voce/'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

resultados = []
for div in soup.find_all('div', {'class': 'const-table-container'}):
    resultados.append(div)

resultados = list(resultados)
resultados = str(resultados[0])

database_link = resultados.split('data-csv-table-renderer-src=')[1].split(' ')[0][1:-1]
print(database_link)
df = pd.read_csv(database_link, delimiter=';')
print(df.head())
