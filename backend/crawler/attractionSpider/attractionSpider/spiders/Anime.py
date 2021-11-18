import scrapy


class AnimeSpider(scrapy.Spider):
    name = 'Anime'
    allowed_domains = ['myanimelist.net']
    start_urls = ['http://myanimelist.net/']

    def parse(self, response):
        pass
