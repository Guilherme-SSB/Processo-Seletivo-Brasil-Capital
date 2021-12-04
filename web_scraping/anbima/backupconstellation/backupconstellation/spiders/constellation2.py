import scrapy


class Constellation2Spider(scrapy.Spider):
    name = 'constellation2'
    allowed_domains = ['www.mudar.com.br']
    start_urls = ['http://www.mudar.com.br/']

    def parse(self, response):
        pass
