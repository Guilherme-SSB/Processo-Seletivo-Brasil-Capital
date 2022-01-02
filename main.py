# Importações
import json
import os
from json.decoder import JSONDecodeError

import pandas as pd

from config import PROJECT_PATH
from integracao_python_excel.python_excel import atualiza_tabela
from integracao_python_sql.python_sql import atualiza_sql
from web_scraping.CVM_backup.webscraping_backup import scraping_backup

os.system('cls')
os.chdir(PROJECT_PATH)

# Coletar dados das gestoras
gestoras = ['dynamo', 'nucleo', 'constellation']

# Para cada gestora na lista das gestoras, faça o web scraping, atualize o SQL Server e a tabela Excel
for gestora in gestoras:
    print(f'Obtendo dados da {gestora}\n\n')
    os.chdir(f'web_scraping/{gestora}')
    # Tenta adquirir os dados, utilizando o Scrapy, a partir dos sites das gestoras
    try:
        if (gestora == 'dynamo') or (gestora == 'nucleo'):
            os.system(f'scrapy crawl ws{gestora} -O ../rentabilidades_resultados/rentabilidades_{gestora}.json')

        if gestora == 'constellation':
            os.system('python webscraping_constellation.py')

        # Verifica se os arquivos JSON não estão vazios
        arquivo = open(PROJECT_PATH + f'/web_scraping/rentabilidades_resultados/rentabilidades_{gestora}.json')

        # Tenta carregar os dados gerados.
        try:
            # Se for possível, atualiza o SQL Server e a tabela Excel
            dados = json.load(arquivo)
            print('\nDados adquiridos com sucesso!')
            atualiza_sql(gestora=gestora.capitalize(),
                         rentabilidade_dia=dados[0]['rentabilidade_dia'].split('%')[0].replace(',', '.'))
            atualiza_tabela(gestora=gestora,
                            rentabilidade_dia=dados[0]['rentabilidade_dia'].split('%')[0].replace('.', ','),
                            rentabilidade_ano=dados[0]['rentabilidade_ano'].split('%')[0].replace('.', ',')
                            )
        except JSONDecodeError:
            # Se houver algum erro (arquivo vazio), tenta coletar os dados a partir do site da CVM
            print(f'\nErro ao adquirir dados pelo site da {gestora}. Tentando a partir do site da CVM\n\n')
            scraping_backup(gestora=gestora)
            dados = json.load(arquivo)
            atualiza_sql(gestora=gestora.capitalize(),
                         rentabilidade_dia=dados['rentabilidade_dia'].split('%')[0].replace(',', '.'))
            atualiza_tabela(gestora=gestora,
                            rentabilidade_dia=dados['rentabilidade_dia'].split('%')[0].replace('.', ','),
                            rentabilidade_ano=None)

    except:
        raise print(f'Houve algum problema na coleta a partir do site da {gestora}\n\n')

    os.chdir(PROJECT_PATH)

# Mostrando tabela de resultados
tabela = pd.read_excel(PROJECT_PATH + '/tabela_rentabilidades.xlsx')
print(tabela.head())
