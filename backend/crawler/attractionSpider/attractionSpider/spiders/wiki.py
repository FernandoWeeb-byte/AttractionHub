import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    #allowed_domains = ['wikipedia.org']
    #start_urls = ['https://pt.wikipedia.org/wiki/Shingeki_no_Kyojin']

    def start_requests(self, response):
        url = response.url
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = response.css('#firstHeading i').get().replace('<i>', '')
        print(name)
