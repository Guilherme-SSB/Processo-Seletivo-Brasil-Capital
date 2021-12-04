import scrapy


class WsnucleoSpider(scrapy.Spider):
    name = 'wsnucleo'
    start_urls = ['http://www.nucleocapital.com.br//']

    def parse(self, response):
        yield{
        'rentabilidade_dia' : response.css('td:nth-child(3)::text').get().replace(',', '.'),
        'rentabilidade_ano' : response.css('td:nth-child(6)::text').get().replace(',', '.') 
        }
