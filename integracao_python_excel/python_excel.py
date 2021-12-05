def atualiza_tabela(gestora: str, rentabilidade_dia: float, rentabilidade_ano: float):
    # Importações
    import json
    import pandas as pd
    from config import PROJECT_PATH

    # Lendo a tabela excel
    tabela = pd.read_excel(PROJECT_PATH + '/tabela_rentabilidades.xlsx')

    # Adquirindo informações
    print('Salvando informações na tabela Excel')
    arquivo = open(PROJECT_PATH + f'/web_scraping/rentabilidades_resultados/rentabilidades_{gestora}.json')
    dados = json.load(arquivo)


    # Atualizando tabela
    tabela.loc[tabela['Gestora']==gestora.capitalize(), 'Rentabilidade Dia'] = rentabilidade_dia
    tabela.loc[tabela['Gestora']==gestora.capitalize(), 'Rentabilidade no Ano'] = rentabilidade_ano
    
    # Fechando arquivo JSON
    arquivo.close()
  
    # Salvando alterações no arquivo EXCEL
    tabela.to_excel(PROJECT_PATH + '/tabela_rentabilidades.xlsx', sheet_name='Projeto_2021', index=False)



if __name__ == '__main__':
    atualiza_tabela()
