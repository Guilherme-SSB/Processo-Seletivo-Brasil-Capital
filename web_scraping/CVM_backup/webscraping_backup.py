def scraping_backup(gestora: str):
    print('Iniciando web scraping de backup')

    # Importações
    import pandas as pd
    import json
    from config import PROJECT_PATH
    import datetime

    # Definições de funções de aquisicão dos dados
    def busca_informes_cvm(ano, mes):
        url = 'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_{:02d}{:02d}.csv'.format(ano,mes)
        return pd.read_csv(url, sep=';')

    def busca_cadastro_cvm():
        url = "http://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv"
        return pd.read_csv(url, sep=';', encoding='ISO-8859-1')

    # Obtendo dados dos fundos do mês e ano atual
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    mes = int(date.strftime("%m"))
    ano = int(date.strftime("%Y"))
    print(mes, ano)
    informes_diarios = busca_informes_cvm(ano, mes)

    # Apenas me interessa os seguintes fundos das gestoras:
    ## CONSTELLATION MASTER FUNDO DE INVESTIMENTO DE AÇÕES -> CNPF: 11.225.860/0001-40
    ## DYNAMO COUGAR FUNDO DE INVESTIMENTO EM COTAS DE FUNDO DE INVESTIMENTO EM AÇÕES -> CNPF: 73.232.530/0001-39
    ## NÚCLEO MASTER FUNDO DE INVESTIMENTO DE AÇÕES -> CNPF: 14.138.786/0001-12
    ##
    if gestora == 'nucleo':
        informes_diarios = informes_diarios[(informes_diarios['CNPJ_FUNDO']=='14.138.786/0001-12')]

    elif gestora == 'dynamo':
        informes_diarios = informes_diarios[informes_diarios['CNPJ_FUNDO']=='73.232.530/0001-39']

    elif gestora == 'constellation':
        informes_diarios = informes_diarios[informes_diarios['CNPJ_FUNDO']=='11.225.860/0001-40']
    
    else:
        raise print('Gestora inválida')

    

    # Obtendo informações adicionais dos fundos 
    cadastro_cvm = busca_cadastro_cvm()


    # Manipulando os dados
    fundos = informes_diarios.pivot(index='DT_COMPTC', columns='CNPJ_FUNDO', values=['VL_TOTAL', 'VL_QUOTA', 'VL_PATRIM_LIQ', 'CAPTC_DIA', 'RESG_DIA'])
    cotas_normalizadas = fundos['VL_QUOTA']/fundos['VL_QUOTA'].iloc[0]

    fundos_de_interesse = pd.DataFrame()
    fundos_de_interesse['rentabilidade_dia'] = (cotas_normalizadas.iloc[-1].sort_values(ascending=False) - 1)*100


    # Completando DataFrame dos fundos de interesse com o nome do fundo
    for cnpj in fundos_de_interesse.index:
        fundo = cadastro_cvm[cadastro_cvm['CNPJ_FUNDO'] == cnpj]
        fundos_de_interesse.at[cnpj, 'Fundo de Investimento'] = fundo['DENOM_SOCIAL'].values[0]

    # Salvando dados

    for fundo in fundos_de_interesse['Fundo de Investimento']:
        resultados = {
            'rentabilidade_dia': str(round(float(fundos_de_interesse[fundos_de_interesse['Fundo de Investimento'] == fundo]['rentabilidade_dia'].values[0]),2)) + '%'
        }
        arquivo = PROJECT_PATH+'/web_scraping/rentabilidades_resultados/rentabilidades_'+fundo.split(' ')[0].lower().replace('ú', 'u')+'.json'
        
        with open(arquivo, 'w') as fp:
            json.dump(resultados, fp)
