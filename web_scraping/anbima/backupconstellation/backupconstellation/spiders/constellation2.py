import scrapy


class Constellation2Spider(scrapy.Spider):
    name = 'constellation2'
    start_urls = ['http://www.mudar.com.br/']

    def parse(self, response):
        pass
