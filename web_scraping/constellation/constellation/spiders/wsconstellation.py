import scrapy


class WsconstellationSpider(scrapy.Spider):
    name = 'wsconstellation'
    allowed_domains = ['https://constellation.com.br/pra-voce/']
    start_urls = ['http://https://constellation.com.br/pra-voce//']

    def parse(self, response):
        pass
