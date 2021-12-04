import scrapy


class WsnucleoSpider(scrapy.Spider):
    name = 'wsnucleo'
    allowed_domains = ['https://www.nucleocapital.com.br/']
    start_urls = ['http://https://www.nucleocapital.com.br//']

    def parse(self, response):
        pass
