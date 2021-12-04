# Caminho do projeto 
PROJECT_PATH = 'C:/Users/guisa/Desktop/Processo-Seletivo-Brasil-Capital'
#TODO Criar spider para o backup constellation: scrapy genspider constellation2 site.com
# Importações
from json.decoder import JSONDecodeError
import os
import json
os.system('cls')

# Coletar dados das gestoras
# gestoras = ['dynamo', 'constellation', 'nucleo']
gestoras = ['nucleo']

for gestora in gestoras:
    print(f'\nObtendo dados da {gestora}')
    os.chdir(f'web_scraping/{gestora}')
    try:
        # Tenta adquirir os dados, utilizando o Scrapy, a partir dos sites das gestoras
        os.system(f'scrapy crawl ws{gestora} -O ../rentabilidades_resultados/rentabilidades_{gestora}.json')
        
        # Verifica se os arquivos JSON não estão vazios
        arquivo = open(PROJECT_PATH + f'/web_scraping/rentabilidades_resultados/rentabilidades_{gestora}.json')
        try: 
            dados = json.load(arquivo)
            print('\n\nDados adquiridos com sucesso!')
        except JSONDecodeError:
            # Arquivo vazio -> Tenta adquirir dados, utilizando o Scrapy, a partir do site da Anbima
            print(f'\nErro ao adquirir dados pelo site da {gestora}. Tentando a partir do site da Anbima\n')

    except:
        raise print(f'Houve algum problema na coleta a partir do site da {gestora}')
         

    os.chdir(PROJECT_PATH)
