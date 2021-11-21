import scrapy
from scrapy.linkextractors import LinkExtractor
import pandas as pd
from .wiki import WikiSpider

# para rodar o crawler use o comando scrapy crawl
# os argumentos devem ser nome da spider e um -a an, que sera o nome do anime
# exemplo para pegar Attack on titan:
# scrapy crawl Anime -a an='Attack on titan'


class AnimeSpider(scrapy.Spider):
    def __init__(self, an=None, *args, **kwargs):
        super(AnimeSpider, self).__init__(*args, **kwargs)
        self.animeName = an.split()
    name = 'Anime'

    def start_requests(self):
        url = 'https://www.google.com/search?q='
        url += ''.join([i+'+' for i in self.animeName])
        url = url[:-1] 
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        xlink = LinkExtractor()
        wikiLinks = []
        malLinks = []
        for link in xlink.extract_links(response):
            if 'wikipedia' in link.text.lower():
                #print(link)
                wikiLinks.append(link.url)
            if any([i in ['my anime list'] for i in link.text.lower()]):
                print(link)
        for i in wikiLinks:
            if i is not None:
                print(f'resquest - link:{i}')
                yield scrapy.Request(url=i, callback=self.parse_wiki)

    def parse_wiki(self, response):
        name = response.css('#firstHeading i').get().replace('<i>', '').replace('</i>', '')
        description = ''.join([k for k in response.css('.infobox_v2+ p').css('::text').extract()])
        genres = [k for k in response.css('.ambox-content+ .infobox_v2 td+ td').css('::text').extract() if len(k) > 1]
        anime = {'name':name, 'description':description, 'genres':genres}
        yield {'name':name, 'description':description, 'genres':genres}
    
    def parse_mal(self, response):
        pass
        


        
            
        
