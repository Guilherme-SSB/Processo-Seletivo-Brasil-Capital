import scrapy


class WsdynamoSpider(scrapy.Spider):
    name = 'wsdynamo'
    allowed_domains = ['https://www.dynamo.com.br/pt']
    start_urls = ['http://https://www.dynamo.com.br/pt/']

    def parse(self, response):
        pass
