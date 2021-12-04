import scrapy


class Dynamo2Spider(scrapy.Spider):
    name = 'dynamo2'
    start_urls = ['http://www.data.anbima.com.br/fundos/010431/']

    def parse(self, response):
        yield{
        'rentabilidade_dia' : response.css('.fundo-1 td:nth-child(6)::text').get().replace(',', '.'),
        'rentabilidade_ano' : response.css('.fundo-1 td:nth-child(9)').get().split()[1].replace(',', '.')
        }
