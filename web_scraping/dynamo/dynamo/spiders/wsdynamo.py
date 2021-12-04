import scrapy


class WsdynamoSpider(scrapy.Spider):
    name = 'wsdynamo'
    start_urls = ['https://www.dynamo.com.br/pt']

    def parse(self, response):
        yield{
        'rentabilidade_dia' : response.css('.fundo-1 td:nth-child(6)::text').get().replace(',', '.'),
        'rentabilidade_ano' : response.css('.fundo-1 td:nth-child(9)').get().split()[1].replace(',', '.')
        }