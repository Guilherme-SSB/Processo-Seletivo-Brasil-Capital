# Importações
import os

# Coletar dados das gestoras
gestoras = ['nucleo', 'dynamo']

for gestora in gestoras:
    print(f'\nObtendo dados da {gestora}')
    os.chdir(f'web_scraping/{gestora}')
    try:
        os.system(f'scrapy crawl ws{gestora} -O ../rentabilidades_resultados/rentabilidades_{gestora}.json')
        print('\n\nDados adquiridos com sucesso!')
    except:
        raise print('ERRO! Houve algum problema')

    os.chdir('C:/Users/guisa/Desktop/Processo Seletivo Brasil Capital')