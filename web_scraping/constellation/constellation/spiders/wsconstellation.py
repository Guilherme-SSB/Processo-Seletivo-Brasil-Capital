import scrapy


class WsconstellationSpider(scrapy.Spider):
    name = 'wsconstellation'
    start_urls = ['http://constellation.com.br/pra-voce/']

    def parse(self, response):
        yield {
            'rentabilidade_dia': response.css('tr:nth-child(1) td:nth-child(5)::text').get().replace(',', '.'),
            'rentabilidade_ano': response.css('tr:nth-child(1) td:nth-child(8)::text').get().replace(',', '.')
        }
