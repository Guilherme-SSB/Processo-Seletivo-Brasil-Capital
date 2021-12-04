import scrapy


class Dynamo2Spider(scrapy.Spider):
    name = 'dynamo2'
    start_urls = ['https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/InfDiario/CPublicaInfDiario.aspx?PK_PARTIC=51091&COMPTC=']

    def parse(self, response):
        rentabilidade_dia_2 = float(response.css('#dgDocDiario tr:nth-child(3) td:nth-child(2)::text').get().replace('.', '').replace(',', '.'))
        rentabilidade_dia_1 = float(response.css('#dgDocDiario tr:nth-child(2) td:nth-child(2)::text').get().replace('.', '').replace(',', '.'))
        rentabilidade_dia = 100*(rentabilidade_dia_2-rentabilidade_dia_1)/rentabilidade_dia_1
        yield{
        'rentabilidade_dia' : f'{rentabilidade_dia}',
        'rentabilidade_ano' : response.css('.fundo-1 td:nth-child(9)').get().split()[1].replace(',', '.')
        }
