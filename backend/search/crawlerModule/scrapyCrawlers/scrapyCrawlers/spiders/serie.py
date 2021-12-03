import scrapy
from scrapy.linkextractors import LinkExtractor
import requests
from ..pipelines import ScrapycrawlersPipeline
from ..items import ScrapycrawlersItem
# para rodar o crawler use o comando scrapy crawl
# os argumentos devem ser nome da spider e um -a an, que sera o nome do anime
# exemplo para pegar Attack on titan:
# scrapy crawl Anime -a an='Attack on titan'


class SerieSpider(scrapy.Spider):
    custom_settings = {
       'ITEM_PIPELINES' :{ScrapycrawlersPipeline: 300,}
    }
    def __init__(self,at=None,tp=None, md=1, *args, **kwargs):
        super(SerieSpider, self).__init__(*args, **kwargs)
        self.attractionName = at.split()
        self.maxDep = int(md)
        self.type = tp
        self.attraction = ScrapycrawlersItem()
        
    name = 'serie'

    def start_requests(self):
        url = 'https://www.google.com/search?q='
        url += ''.join([i+'+' for i in self.attractionName])
        url1 = url+'justwatch "us"'
        url2 = url+'justwatch'
        yield scrapy.Request(url=url1, callback=self.getLink,meta={'domain':'justwatch.com','name':'justwatchEn'})
        yield scrapy.Request(url=url2, callback=self.getLink,meta={'domain':'justwatch.com','name':'justwatch'})


    def getLink(self, response):
        xlink = LinkExtractor()
        links = []
        for l in xlink.extract_links(response):
            if response.meta['domain'] in l.url:
                links.append(l.url)
        #print(links)
        if len(links) > self.maxDep:
            lim = self.maxDep
        else:
            lim = len(links)
        #print(lim)
        for i in range(lim):
            url = links[i]
            if url is not None:
                #print(f'resquest - link:{i}')
                if response.meta['name'] == 'justwatchEn':
                    yield scrapy.Request(url=url, callback=self.parse_just_watch)
                if response.meta['name'] == 'justwatch':
                    yield scrapy.Request(url=url, callback=self.parse_streaming)


    def parse_just_watch(self,response):
        en_name = response.css('h1::text').get()
        url_img = response.css('.title-poster--no-radius-bottom  .lazyload::attr(data-src)').get()
        desc = response.css('.jw-info-box__container-content div div div p.text-wrap-pre-line span::text').get()
        if desc == None:
            desc = response.css('.jw-info-box__container-content div div div p.text-wrap-pre-line::text').get()
        genres = response.css('.title-info .detail-infos .detail-infos__value span::text').getall()
        genres = list(filter(lambda x: (x != ", "), genres))
        genres = list(dict.fromkeys(genres))
        rating = response.css('.detail-infos:nth-child(5) .detail-infos__value::text').get()

        justWatchDict = {'en_name': en_name,'desc': desc, 'url_img': url_img, 'genres': genres, 'rating': rating,'type': self.type} 
       
        

        requests.get('http://127.0.0.1:8000/list/serie/', data=justWatchDict)
        yield justWatchDict
        
    def parse_streaming(self,response):
        stream = response.css('.price-comparison--block .price-comparison__grid__row__holder div div img::attr(alt)').getall()
        streamDict = {'stream':stream}
        yield streamDict
    
